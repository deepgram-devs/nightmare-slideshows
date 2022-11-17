# boringslideshows.no

You will need to install `gunicorn`, `ffmpeg`, `pip install flask flask-cors`, and `pip install git+https://github.com/openai/whisper.git`.

Run with:

```
gunicorn app:app
```

Also, maybe, modify `.flaskenv` as suits your needs.

## Frontend Setup

First, `cd frontend`.

Install dependencies: `npm install`

Run hot-reloading dev build: `npm run dev`

Compile for production: `npm run build`

## Deployment 
run `docker-compose up -d` on the server and nginx will listen on 80 & 443
you should be able to hit https://boringslideshows.no.deepgram.com

Adjust site paths in site.conf and place that in `/data/sites` on the host
Deploy frontend code to `/data/www` this will be served up by nginx