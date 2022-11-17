"""
import torch

from diffusers import StableDiffusionPipeline

model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda"

pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe = pipe.to(device)
"""

# Create a list of images and return the list of saved filenames 
# in the same order as the utterances in the transcript
def text_to_images(pipe, utterances):
    for utt in utterances:
        print(utt)
        # prompt = utt['transcript']
        # image = pipe(prompt, num_inference_steps=5).images[0]
        # image.save("astronaut_rides_horse.png")
    return utterances


"""
https://developers.deepgram.com/documentation/features/utterances/

"utterances":[
  {
    "start":0.41915998,
    "end":5.43012,
    "confidence":0.88172823,
    "channel":0,
    "transcript":"four score and seven years ago our fathers brought forth on this continent a new nation",
    "words":[
      {"word":"four","start":0.41915998,"end":0.85827994,"confidence":0.57893836},
      {"word":"score","start":0.85827994,"end":1.13772,"confidence":0.9444983},
      {"word":"and","start":1.13772,"end":1.33732,"confidence":0.9409597},
      {"word":"seven","start":1.33732,"end":1.5768399,"confidence":0.9984718},
      {"word":"years","start":1.5768399,"end":1.8962,"confidence":0.9997415},
      {"word":"ago","start":1.8962,"end":2.0958,"confidence":0.999086},
      {"word":"our","start":2.41516,"end":2.65468,"confidence":0.97390944},
      {"word":"fathers","start":2.65468,"end":3.15468,"confidence":0.4639914},
      {"word":"brought","start":3.1736398,"end":3.4131598,"confidence":0.9835603},
      {"word":"forth","start":3.4131598,"end":3.6925998,"confidence":0.9952933},
      {"word":"on","start":3.6925998,"end":3.85228,"confidence":0.6618892},
      {"word":"this","start":3.85228,"end":4.05188,"confidence":0.83480215},
      {"word":"continent","start":4.05188,"end":4.55188,"confidence":0.7847378},
      {"word":"a","start":4.6107597,"end":4.7704396,"confidence":0.9857173},
      {"word":"new","start":4.7704396,"end":4.93012,"confidence":0.9722444},
      {"word":"nation","start":4.93012,"end":5.43012,"confidence":0.9898116}
    ],
    "id":"2d8211a4-3a5b-4053-8939-edf2b2b389fa"
  },
  {
    "start":5.8882,
    "end":9.880199,
    "confidence":0.9834162,
    "channel":0,
    "transcript":"conceived liberty and dedicated to the proposition that all men are created equal",
    "words":[
      {"word":"conceived","start":5.8882,"end":6.2075596,"confidence":0.99398476},
      {"word":"liberty","start":6.2075596,"end":6.7075596,"confidence":0.9671354},
      {"word":"and","start":6.7265196,"end":6.8862,"confidence":0.94633394},
      {"word":"dedicated","start":6.8862,"end":7.32532,"confidence":0.99565625},
      {"word":"to","start":7.32532,"end":7.44508,"confidence":0.9971002},
      {"word":"the","start":7.44508,"end":7.56484,"confidence":0.9988673},
      {"word":"proposition","start":7.56484,"end":8.06484,"confidence":0.9360018},
      {"word":"that","start":8.16364,"end":8.363239,"confidence":0.99458367},
      {"word":"all","start":8.363239,"end":8.602759,"confidence":0.9973457},
      {"word":"men","start":8.602759,"end":8.92212,"confidence":0.9911361},
      {"word":"are","start":8.92212,"end":9.161639,"confidence":0.9973839},
      {"word":"created","start":9.161639,"end":9.56084,"confidence":0.9712871},
      {"word":"equal","start":9.56084,"end":9.880199,"confidence":0.9975957}
    ],
    "id":"e88264de-a8cf-44e9-a7db-848ad5bab7a5"
  },
  {
    "start":10.648263,
    "end":17.190998,
    "confidence":0.9015952,
    "channel":0,
    "transcript":"now we are engaged in a great civil war testing whether that nation or any nations open conceived and so dedicated can long endure",
    "words":[
      {"word":"now","start":10.648263,"end":10.887631,"confidence":0.998248},
      {"word":"we","start":10.887631,"end":11.007316,"confidence":0.9859103},
      {"word":"are","start":11.007316,"end":11.246684,"confidence":0.9960179},
      {"word":"engaged","start":11.246684,"end":11.4860525,"confidence":0.99533737},
      {"word":"in","start":11.4860525,"end":11.565842,"confidence":0.988396},
      {"word":"a","start":11.565842,"end":11.765315,"confidence":0.8131491},
      {"word":"great","start":11.765315,"end":12.0046835,"confidence":0.9668163},
      {"word":"civil","start":12.0046835,"end":12.323841,"confidence":0.9583378},
      {"word":"war","start":12.323841,"end":12.523315,"confidence":0.99313295},
      {"word":"testing","start":12.722789,"end":13.081841,"confidence":0.9985874},
      {"word":"whether","start":13.081841,"end":13.361105,"confidence":0.99108666},
      {"word":"that","start":13.361105,"end":13.520683,"confidence":0.97984374},
      {"word":"nation","start":13.520683,"end":13.919631,"confidence":0.9745518},
      {"word":"or","start":13.919631,"end":14.039315,"confidence":0.9277347},
      {"word":"any","start":14.039315,"end":14.278684,"confidence":0.9939051},
      {"word":"nations","start":14.278684,"end":14.637736,"confidence":0.39617103},
      {"word":"open","start":14.637736,"end":14.996789,"confidence":0.4592044},
      {"word":"conceived","start":14.996789,"end":15.156368,"confidence":0.85864764},
      {"word":"and","start":15.156368,"end":15.355842,"confidence":0.6100463},
      {"word":"so","start":15.355842,"end":15.515421,"confidence":0.98514366},
      {"word":"dedicated","start":15.515421,"end":16.01542,"confidence":0.99832517},
      {"word":"can","start":16.313314,"end":16.552683,"confidence":0.8627608},
      {"word":"long","start":16.552683,"end":16.911736,"confidence":0.9811041},
      {"word":"endure","start":16.911736,"end":17.190998,"confidence":0.92582434}
    ],
    "id":"1e60a5d3-b537-4627-8334-7256e341ef67"
  }
]


"""