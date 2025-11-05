import speech_recognition as sr
import time
from urllib.error import URLError


def get_user_text():

    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 1  # seconds of non-speaking audio before a phrase is considered complete
    recognizer.operation_timeout = 4  # increasing the timeout duration
    audio_data = None
    filename = "input.wav"

    while True:
        # record audio only if it hasn't been recorded yet
        if audio_data is None:
#            with NaoAudioSource() as source:
            with sr.Microphone() as source:
                print("Recording...")
                start_time = time.time()
                audio_data = recognizer.listen(source, phrase_time_limit=10, timeout=None)
                with open(filename, "wb") as f:
                    f.write(audio_data.get_wav_data())
                print(f"Recording took {time.time() - start_time} seconds")

         # transcribe audio to text
        try:
            print("Transcribing...")
            start_time = time.time()
            text = recognizer.recognize_google(audio_data)
            print(f"Transcribing took {time.time() - start_time} seconds")
            print("You said: " + text)
            return text
        except (sr.RequestError, URLError, ConnectionResetError) as e:
            print(f"Network error: {e}, retrying after a short delay...")
            time.sleep(sleep_time)  # adding a delay before retrying
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio, retrying...")
            audio_data = None  # reset audio_data to record again
        except TimeoutError as e:
            print(f"Operation timed out: {e}, retrying after a short delay...")
            audio_data = None  # reset audio_data to record again


while True:
    print(get_user_text())
