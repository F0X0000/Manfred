import playsound
import os
from gtts import gTTS

def say(text):
    tts = gTTS(text=text, lang="pl")
    filename = "voice.mp3"
    tts.save(filename)
    print(text)
    playsound.playsound(filename)
    os.remove('voice.mp3')

def lossay(text):
    a = random.choice(text)
    say(a)
