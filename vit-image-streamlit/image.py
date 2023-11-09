import streamlit as st
from transformers import ViTImageProcessor, ViTForImageClassification, ViTFeatureExtractor
from PIL import Image
import torch


st.title('이미지 분류기')

tab1, tab2 = st.tabs(['이미지 종류 분류', '나이 예측'])

with tab1:
    processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224')
    model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')

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

with tab2:
    @st.cache_resource
    def get_model_transforms():
        model = ViTForImageClassification.from_pretrained('nateraw/vit-age-classifier')
        transforms = ViTFeatureExtractor.from_pretrained('nateraw/vit-age-classifier')
        return model, transforms

    model, transforms = get_model_transforms()

    file_name = st.file_uploader('나이를 예측할 이미지를 업로드하세요.', type=['png', 'jpg', 'jpeg'])

    if file_name is not None:
        image = Image.open(file_name)
        st.image(image, use_column_width=True)

        # Transform our image and pass it through the model
        inputs = transforms(image, return_tensors='pt')
        output = model(**inputs)

        # Predicted Class probabilities
        proba = output.logits.softmax(1)

        # Predicted Classes
        preds = proba.argmax(1)

        values, indices = torch.topk(proba, k=5)

        result_dict = {model.config.id2label[i.item()]: v.item() for i, v in zip(indices.numpy()[0], values.detach().numpy()[0])}
        first_result = list(result_dict.keys())[0]

        print(f'predicted result:{result_dict}')
        print(f'1st: {first_result}')

        st.header('결과')
        st.subheader(f'예측된 나이: {first_result}')

        for k, v in result_dict.items():
            st.write(f'{k}: {v * 100:.2f}%')