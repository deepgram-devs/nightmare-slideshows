import flask
import tempfile
import string
import uuid
import re
import datetime
import requests
from flask import jsonify
from flask_cors import CORS

allowed_origins=re.compile('(.*\.)?deepgram\.com(:\d+)?')

app = flask.Flask(__name__)
CORS(app, origins=allowed_origins)

model = whisper.load_model("base")

@app.route('/v1/listen', methods=['POST'])
def transcribe():
    if flask.request.is_json:
        req = flask.request.get_json()
        audio = requests.get(req["url"]).content
    else:
        audio = flask.request.get_data()


