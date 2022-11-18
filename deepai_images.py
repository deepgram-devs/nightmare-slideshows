import os
import urllib
import requests
from dotenv import load_dotenv

load_dotenv()

def text_to_images(transcript, request_dir):
  utterances = transcript['results']['utterances']
  print("no of utterances: {}".format(len(utterances)))
  os.makedirs(request_dir, exist_ok=True)
  filenames = []
  for k, utt in enumerate(utterances):
    r = requests.post(
      "https://api.deepai.org/api/fantasy-world-generator",
      data = {'text': utt['transcript']},
      headers={'api-key': os.environ["DEEPAI_KEY"]}
    )
    print("JSON", r.json())
    image_url = r.json()['output_url']

    filenames.append(f'{request_dir}/{k}.jpg')
    urllib.request.urlretrieve(image_url, filenames[-1])
    
  return filenames



if __name__ == '__main__':
    utts = {'results': {'utterances': [{'transcript': 'hello'}, {'transcript': 'chasing after car'}]}}
    text_to_images(utterances=utts, request_dir='hellohere')
