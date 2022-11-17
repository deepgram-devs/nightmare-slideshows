import os

def text_to_images(utterances, request_dir):
  os.makedirs(request_dir, exist_ok=True)
  filenames = []
  for k, utt in enumerate(utterances):
    filenames.append(f'{request_dir}/{k}.jpg')
    with open(filenames[-1], 'wb') as f_out:
        with open('./frontend/static/logo.png', 'rb') as f_in:
            f_out.write(f_in.read())

  return filenames