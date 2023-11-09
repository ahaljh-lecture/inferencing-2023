from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "너는 dall-e용 prompt 생성 전문가야. 내가 주제를 주면 그 주제를 가지고 dall-e에게 이미지를 생성하기 위한 prompt를 만들어줘. prompt는 영문 단어 모음이어야 하고, 20개 정도의 단어로 만들어줘."},
        {"role": "user", "content": f"주제: 하늘을 날라다니는 눈사람"}
    ],
)

print(f'{completion.choices[0].message.content}')