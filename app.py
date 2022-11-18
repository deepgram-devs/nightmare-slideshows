import flask
from flask import jsonify, request
from flask_cors import CORS
import json
import re
import string
import uuid
import requests
from dotenv import load_dotenv
import os

if os.environ.get("USE_DEEPAI") == "true":
    print("using deepai")
    import deepai_images as generate_images
else:
    print("using stablediffusion")
    import stablediff_images as generate_images

import video

load_dotenv()

allowed_origins=re.compile('(.*\.)?deepgram\.com(:\d+)?')

app = flask.Flask(__name__)
CORS(app, origins="*")

STATIC_DIR = os.environ.get("STATIC_DIR", "./static").rstrip("/")

@app.route('/', methods=['GET', 'POST'])
def transcribe():
    if request.method == 'GET':
        return 'Hello, world!'
    else:
        request_id = uuid.uuid4()
        request_dir=f"{STATIC_DIR}/{request_id}/"

        if flask.request.is_json:
            req = flask.request.get_json()
            audio = requests.get(req["url"]).content
        else:
            audio = flask.request.get_data()

        transcript = fetch_transcript(audio)
        if isinstance(transcript, str):
            # A string response indicates an error.  Return it, and call it a 500 because error handling is boring
            return transcript, 500

        os.mkdir(request_dir)

        audio_path = request_dir + "audio"
        with open(audio_path, "wb") as audiof:
            audiof.write(audio)

        images = generate_images.text_to_images(transcript, request_dir)
        print(images)
        
        output_path = request_dir + "video.mp4"
        video.generate_video(audio_path, transcript, images, output_path)

        return {"path": f"{STATIC_DIR}/{request_id}/video.mp4"}


@app.route('/static/<path:path>', methods=['GET'])
def assets(path):
    return flask.send_from_directory(STATIC_DIR, path)

def fetch_transcript(audio: bytes):
    deepgram_response = requests.post("https://api.deepgram.com/v1/listen?model=general&language=en&tier=enhanced&punctuate=true&utterances=true", headers={
        'Authorization': 'Token {}'.format(os.environ.get("DEEPGRAM_API_KEY"))
    }, data=audio)

    if deepgram_response.ok:
        response = deepgram_response.json()
    else:
        response = deepgram_response.text
    
    return response
