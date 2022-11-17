import torch
from diffusers import StableDiffusionPipeline

model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda"

pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe = pipe.to(device)


# Create a list of images and return the list of saved filenames 
# in the same order as the utterances in the transcript
def text_to_images(utterances):
  filenames = []
  for k, utt in enumerate(utterances):
    image = pipe(utt['transcript'], num_inference_steps=50).images[0]

    filenames.append(f'{k}.jpg')
    image.save(filenames[-1])

  return filenames