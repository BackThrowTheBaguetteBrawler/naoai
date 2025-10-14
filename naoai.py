import os
from openai import OpenAI

def askAi(prompt):
    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("mario"),
        base_url="http://10.13.100.50:1234/v1",
    )
    
    response = client.responses.create(
        model="gpt-4o",
    #    instructions="You are a smart assistant that talks like a pirate.",
        input=f"Answer in a pirate accent: {prompt}",
    )
    (response.output_text)
    return(response.output_text)

print(askAi(input("What will you ask the ai?"))
