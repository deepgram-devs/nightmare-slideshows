# whisper-server

You will need to install `gunicorn`, `ffmpeg`, `pip install flask flask-cors`, and `pip install git+https://github.com/openai/whisper.git`.

Run with:

```
gunicorn app:app
```

Also, maybe, modify `.flaskenv` as suits your needs.
