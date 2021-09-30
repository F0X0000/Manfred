import speech_recognition as sr
import os

xx = "0"

def get_audio():
    xx = "0"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Nasłuchuję...")
        audio = r.listen(source)
        said=""
        try:
            said= r.recognize_google(audio, language="pl")
            print("Powiedziałeś: " + said.lower())
            xxx("1")
        except Exception as e:
            print("Czekam na komendę..." + str(e))
            xxx("0")

    return said.lower()

def xxx(a):
    f1 = open("pliki/101.txt", "a+")
    f1.write(a)
    f1.close()

def xdx():
    f2 = open("pliki/101.txt", "a+")
    f2.close()
    os.remove('pliki/101.txt')
