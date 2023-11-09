from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# client = OpenAI(api_key='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')
client = OpenAI()

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# stream = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "너는 시인이야. 창의적이고 세상을 아름답게 잘 표현하는 시인이야."},
#     {"role": "user", "content": "가을을 주제로 시를 써줘"}
#   ],
#   stream=True,
# )

stream = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "너는 의사결정할 때 도움을 주는 비서야."},
    {"role": "user", "content": "오늘 점심식사 메뉴로 어떤 것이 좋을까? 메뉴 1개만 짧게 대답해줘."}
  ],
  stream=True,
  max_tokens=100,
  temperature=0.9,
)

print('completion')

for part in stream:
  print(f'part: {part}')
#   print(part.choices[0].delta.content or "", end="")

# print(completion.choices[0].message)

# print(completion.choices[0].message.content)