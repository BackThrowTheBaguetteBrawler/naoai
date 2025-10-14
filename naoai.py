import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("mario"),
    base_url="http://10.13.100.50:1234/v1",
)

response = client.responses.create(
    model="gpt-4o",
#    instructions="You are a smart assistant that talks like a pirate.",
    input="Answer in a pirate accent: Who created super mario?",
)

print(response.output_text)
