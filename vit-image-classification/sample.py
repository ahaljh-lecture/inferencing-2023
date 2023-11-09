from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image
import requests
import torch

url = 'http://images.cocodataset.org/val2017/000000039769.jpg'
image = Image.open(requests.get(url, stream=True).raw)

processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224')
model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')

inputs = processor(images=image, return_tensors="pt")
outputs = model(**inputs)
logits = outputs.logits
# model predicts one of the 1000 ImageNet classes
predicted_class_idx = logits.argmax(-1).item()
predicted_class = model.config.id2label[predicted_class_idx]
print("Predicted class:", predicted_class)

proba = logits.softmax(1)
values, indices = torch.topk(proba, k=5)

result_dict = {model.config.id2label[i.item()]: v.item() for i, v in zip(indices.numpy()[0], values.detach().numpy()[0])}

print(f'predicted result:{result_dict}')