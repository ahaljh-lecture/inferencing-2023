from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.images.generate(
  model="dall-e-2",
  prompt="Polar Bear with a Cola",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)
print('-------')
print(response)
