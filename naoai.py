serverIP="10.13.100.50"
robotIP="10.13.100.49"

import os
import sys
import qi
from openai import OpenAI

def askAi(prompt):
    client = OpenAI(
        # This is the default and can be omitted
        api_key="mario",
        base_url=f"http://{serverIP}:1234/v1",
    )
    
    response = client.responses.create(
        model="gpt-4o",
    #    instructions="You are a smart assistant that talks like a pirate.",
        input=f"Answer in a pirate accent: {prompt}",
#        input=f"Answer in a gen-alpha skibidi sigma brainrot rizz accent: {prompt}",
    )
    (response.output_text)
    return(response.output_text)

def connectToNao():
    # Connect to the robot
    session = qi.Session()
    session.connect(f"tcp://{robotIP}:9559")
    
    # Create a proxy to the ALTextToSpeech service
    tts = session.service("ALTextToSpeech")

# Use the text-to-speech service
#connectToNao()
#tts.say(askAi(sys.argv[1]))
print(askAi(sys.argv[1]))
