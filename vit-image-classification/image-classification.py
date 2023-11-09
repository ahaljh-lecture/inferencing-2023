import streamlit as st
from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image
import torch

processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224')
model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')


st.title('이미지를 분류합니다.')

file_name = st.file_uploader('이미지를 업로드하세요.', type=['png', 'jpg', 'jpeg'])

if file_name is not None:
    image = Image.open(file_name)
    st.image(image, use_column_width=True)

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

    st.header('결과')
    st.subheader(f'예측 결과: {predicted_class}')

    for k, v in result_dict.items():
        st.write(f'{k}: {v * 100:.2f}%')