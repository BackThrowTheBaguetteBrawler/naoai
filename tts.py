import sys
from naoqi import ALProxy

# Replace '<IP of your robot>' with the actual IP address of your NAO
tts = ALProxy("ALTextToSpeech", "<IP of your robot>", 9559)
tts.say("Hello, world!")

