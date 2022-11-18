import os
import torch
from diffusers import StableDiffusionPipeline
from dotenv import load_dotenv

load_dotenv()

model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda"

pipe = StableDiffusionPipeline.from_pretrained(model_id, use_auth_token=os.environ.get("HUGGINGFACE_TOKEN"))
pipe = pipe.to(device)


# Create a list of images and return the list of saved filenames 
# in the same order as the utterances in the transcript
def text_to_images(transcript, request_dir):
  utterances = transcript['results']['utterances']
  print("no of utterances: {}".format(len(utterances)))
  os.makedirs(request_dir, exist_ok=True)
  filenames = []
  for k, utt in enumerate(utterances):
    image = pipe(utt['transcript'], num_inference_steps=50).images[0]

    filenames.append(f'{request_dir}/{k}.jpg')
    image.save(filenames[-1])

  return filenames


if __name__ == '__main__':
    utts = {'results': {'utterances': [{'transcript': 'hello'}, {'transcript': 'chasing after car'}]}}
    text_to_images(utterances=utts, request_dir='hellohere')
