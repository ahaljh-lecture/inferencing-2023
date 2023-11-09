import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

st.title('이미지를 생성해봅시다.')
st.caption('ChatGPT와 Dall-E를 이용해 이미지를 생성합니다. :smile:')

image_subject = st.text_input('이미지를 생성할 주제를 입력하세요.')
if st.button('이미지 생성'):

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "너는 창의적인 dall-e용 프롬프트 생성 전문가야. 내가 입력하는 주제를 가지고 dall-e에게 이미지를 생성하기 위한 프롬프트를 만들어줘. 100자 이내의 영문으로 만들어줘."},
            {"role": "user", "content": f"주제: {image_subject}"}
        ],
    )

    dalle_prompt = completion.choices[0].message.content
    st.write(dalle_prompt)

    response = client.images.generate(
        model="dall-e-2",
        # prompt="Polar Bear with a Cola",
        prompt=dalle_prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    st.image(image_url)
    print('-------')
    print(response)