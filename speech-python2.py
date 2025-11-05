# -*- coding: utf-8 -*-
from __future__ import print_function
import speech_recognition as sr
import time
import urllib2  # urllib2 for Python 2

def get_user_text():
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 1  # seconds of non-speaking audio before a phrase is considered complete
    recognizer.operation_timeout = 4  # increasing the timeout duration
    audio_data = None
    filename = "input.wav"
    sleep_time = 3  # define a short delay before retrying

    while True:
        # record audio only if it hasn't been recorded yet
        if audio_data is None:
            with sr.Microphone() as source:
                print("Recording...")
                start_time = time.time()
                audio_data = recognizer.listen(source, phrase_time_limit=10, timeout=None)
                with open(filename, "wb") as f:
                    f.write(audio_data.get_wav_data())
                print("Recording took {} seconds".format(time.time() - start_time))

        # transcribe audio to text
        try:
            print("Transcribing...")
            start_time = time.time()
            text = recognizer.recognize_google(audio_data)
            print("Transcribing took {} seconds".format(time.time() - start_time))
            print("You said: " + text)
            return text

        except (sr.RequestError, urllib2.URLError, IOError) as e:
            print("Network error: {}, retrying after a short delay...".format(e))
            time.sleep(sleep_time)  # adding a delay before retrying

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio, retrying...")
            audio_data = None  # reset audio_data to record again

        except IOError as e:
            print("Operation timed out: {}, retrying after a short delay...".format(e))
            audio_data = None  # reset audio_data to record again


while True:
    print(get_user_text())
