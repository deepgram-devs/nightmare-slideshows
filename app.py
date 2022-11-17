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

load_dotenv()

allowed_origins=re.compile('(.*\.)?deepgram\.com(:\d+)?')

app = flask.Flask(__name__)
CORS(app, origins="*")

@app.route('/', methods=['GET', 'POST'])
def transcribe():
    if request.method == 'GET':
        return 'Hello, world!'

    else:
        #print(dir(uuid))
        #request_id = uuid.UUID4()

        if flask.request.is_json:
            req = flask.request.get_json()
            audio = requests.get(req["url"]).content
        else:
            audio = flask.request.get_data()

        transcript = fetch_transcript(audio)
        images = generate_images(transcript)

        return transcript

        #audio_path = ...
        #transcript_path = ...

        #video.generate_video(audio_path, transcript_path, images)

def fetch_transcript(audio: bytes):
    deepgram_response = requests.post("https://api.deepgram.com/v1/listen?model=general&language=en&tier=enhanced&punctuate=true&utterances=true", headers={
        'Authorization': 'Token {}'.format(os.environ.get("DEEPGRAM_API_KEY"))
    }, data=audio)

    if deepgram_response.ok:
        response = deepgram_response.json()['results'].get('utterances', [])
    else:
        response = deepgram_response.text
    
    return response


def generate_images(transcript_json):
    pass
