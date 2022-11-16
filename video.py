import itertools 
import json
from typing import Iterable
from pathlib import Path

from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips


def generate_video(audio_path: str, transcript_path: str, images: Iterable[str], output_path: Path):
    '''
    Construct a video that switches between the provided images at the boundaries 
    of the utterances in the provided transcript.  The original audio should also be provided.

    output_path is the name of the file to save the audio as.
    '''
    transcript = json.load(open(transcript_path))
    utts = transcript['results']['utterances']

    clips = []
    for (utt, image, next) in zip(utts, itertools.cycle(images), itertools.chain(utts[1:], [None])):
        start = utt['start']
        if start < 1.0:
            start = 0.0
        if next:
            end = next['start']
        else:
            end = utt['end']
        duration = end - start 
        clips.append(ImageClip(image).set_duration(duration * 3).set_fps(24))

    final = concatenate_videoclips(clips)
    final.audio = AudioFileClip(audio_path)
    final.write_videofile(output_path)


if __name__ == '__main__':
    images = [
        "/home/cliff/Pictures/emile-zola.jpg", 
        "/home/cliff/Pictures/gorgonzola.jpg", 
    ]

    generate_video(
        "/home/cliff/Music/youtoobio-cannibal-toads.mp3",
        "./toads.json",
        images,
        "./toads-functional.mp4",
    )

