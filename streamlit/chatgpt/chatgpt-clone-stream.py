import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


st.title('ChatGPT 따라 만들기')

st.subheader('챗봇을 만들어봅시다.')

prompt = st.chat_input(placeholder='메시지를 입력하세요.')

# 시작 메시지
with st.chat_message('ai'):
    st.write('안녕하세요. 무엇을 도와드릴까요? :smile:')

if st.session_state.get('chat_messages') is None:
    st.session_state.chat_messages = []

for message in st.session_state.chat_messages:
    with st.chat_message(message['sender']):
        st.write(message['text'])

if prompt:
    with st.chat_message('user'):
        st.write(prompt)
    st.session_state.chat_messages.append({'sender': 'user', 'text': prompt})

    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "너는 뭐든 척척 잘 대답하는 비서야. 근데 대답할 때 길지 않게 간결하게 대답해줘."},
            {"role": "user", "content": f"{prompt}"}
        ],
        stream=True,
    )

    with st.chat_message('ai'):
        full_response = ''
        placeholder = st.empty()
        for part in stream:
            print(f'part: {part}')
            part_response = part.choices[0].delta.content or ""
            # st.write(part_response)
            full_response += part_response
            placeholder.text(full_response)
        
    st.session_state.chat_messages.append({'sender': 'ai', 'text': full_response})
    