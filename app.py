import flask
import tempfile
import string
import uuid
import re
import datetime
import requests
from flask import jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import video
import os
import generate_images

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
        request_dir=f"{STATIC_DIR}/{request_uuid}/"

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
        with open(audio_path, "w") as audiof:
            audiof.write(audio)

        images = generate_images.text_to_images(False, transcript, request_dir)
        print(images)
        
        output_path = request_dir + "video.mp4"
        #video.generate_video(audio_path, transcript, images, output_path)

        return transcript


def fetch_transcript(audio: bytes):
    deepgram_response = requests.post("https://api.deepgram.com/v1/listen?model=general&language=en&tier=enhanced&punctuate=true&utterances=true", headers={
        'Authorization': 'Token {}'.format(os.environ.get("DEEPGRAM_API_KEY"))
    }, data=audio)

    if deepgram_response.ok:
        response = deepgram_response.json()['results'].get('utterances', [])
    else:
        response = deepgram_response.text
    
    return response
