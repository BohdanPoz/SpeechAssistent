import pyttsx3
import os
from utils import read_json

def text_to_speech(text, languages):
    settings_languages = read_json(os.path.abspath(__file__+'/..')+'\\settings\\languages.json')[languages]

    engine = pyttsx3.init()
    
    #set voice
    voices = voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[settings_languages["index"]].id)

    #say text
    engine.say(text)
    engine.runAndWait()
