import requests
from PIL import Image
from io import BytesIO
import torch

from transformers import ViTFeatureExtractor, ViTForImageClassification

# Get example image from official fairface repo + read it in as an image
r = requests.get('https://github.com/dchen236/FairFace/blob/master/detected_faces/race_Asian_face0.jpg?raw=true')
im = Image.open(BytesIO(r.content))

# Init model, transforms
model = ViTForImageClassification.from_pretrained('nateraw/vit-age-classifier')
transforms = ViTFeatureExtractor.from_pretrained('nateraw/vit-age-classifier')

# Transform our image and pass it through the model
inputs = transforms(im, return_tensors='pt')
output = model(**inputs)

# Predicted Class probabilities
proba = output.logits.softmax(1)

values, indices = torch.topk(proba, k=5)

result_dict = {model.config.id2label[i.item()]: v.item() for i, v in zip(indices.numpy()[0], values.detach().numpy()[0])}
first_result = list(result_dict.keys())[0]

print(f'predicted result:{result_dict}')
print(f'first_result: {first_result}')