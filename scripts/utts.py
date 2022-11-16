import itertools
import json

def print_utterances(transcript_path: str):

    transcript = json.load(open(transcript_path))
    utts = transcript['results']['utterances']

    clips = []
    for (utt, next) in zip(utts, itertools.chain(utts[1:], [None])):
        start = utt['start']
        if start < 1.0:
            start = 0.0
        if next:
            end = next['start']
        else:
            end = utt['end']
        duration = end - start 
        print(start, end, utt['transcript'])


if __name__ == '__main__':
    import sys
    print_utterances(sys.argv[1])

