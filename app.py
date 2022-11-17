import flask
import tempfile
import string
import uuid
import re
import datetime
import requests
from flask import jsonify
from flask_cors import CORS

import video

allowed_origins=re.compile('(.*\.)?deepgram\.com(:\d+)?')

app = flask.Flask(__name__)
CORS(app, origins=allowed_origins)

model = whisper.load_model("base")

from .
@app.route('/', methods=['POST'])
def transcribe():
    print(dir(uuid))
    request_id = uuid.UUID4()

    if flask.request.is_json:
        req = flask.request.get_json()
        audio = requests.get(req["url"]).content
    else:
        audio = flask.request.get_data()

    transcript = fetch_transcript(audio)
    images = generate_images(transcript)

    audio_path = ...
    transcript_path = ...

    video.generate_video(audio_path, transcript_path, images)


def fetch_transcript(audio: bytes):
    pass

def generate_images(transcript_json):
    pass
