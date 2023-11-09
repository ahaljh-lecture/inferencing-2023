import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

st.title('광고문구 생성기')

st.subheader('광고문구를 생성해보세요.')

product_name = st.text_input('제품명을 입력하세요.')
feature1 = st.text_input('제품의 특징이나 장점을 입력해주세요.(3가지)', key='feature1')
feature2 = st.text_input('-', key='feature2', label_visibility='collapsed')
feature3 = st.text_input('--', key='feature3', label_visibility='collapsed')
option = st.selectbox('광고문구의 스타일을 선택하세요.', ['심플한', '부드러운', '과장된'])

if st.button('광고문구 생성'):
    prompt = f''' ## 광고문구를 생성해줘. 광고 문구를 만들 때 {option} 스타일로 부탁해.
* 제품명 : {product_name}
* 특징 및 장점
    * {feature1}
    * {feature2}
    * {feature3}
'''
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "너는 광고문구 생성기야. 제품명과 제품의 설명, 그리고 광고문구 스타일을 입력받아 광고문구를 생성해줘."},
            {"role": "user", "content": f"{prompt}"}
        ],
    )

    st.write(f'{completion.choices[0].message.content}')
    st.toast('광고문구 생성 완료')