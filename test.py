import speech_recognition as sr 
import pyaudio
import pywhatkit
# the ability of a machine or program to identify words spoken aloud and convert them into readable text
def get_audio():
    recorder = sr.Recognizer()#The recognizer performs this operation against its loaded and enabled speech recognition grammars.
    with sr.Microphone() as source:
        print("say something.........")
        audio = recorder.listen(source)

    text = recorder.recognize_google(audio)# access the Google web speech API and turn spoken language into text
    print(f"you said: {text}")
    return text

get_audio()

text = get_audio()

if "youtube" in text.lower():
    pywhatkit.playonyt(text)
else:
    pywhatkit.search(text)
    