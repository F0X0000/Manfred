def setup():
    import os
    r = ["t"]
    f = open("pliki/install.txt", "r+")
    fr = f.read(1)
    if fr in r:
        print(" ")
        f.close()
    else:
        os.system("PyAudio-0.2.11-cp39-cp39-win_amd64.whl")
        os.system("pip install SpeechRecognition")
        os.system("pip install PyAudio")
        os.system("pip install playsound")
        os.system("pip install gTTS")
        os.system("cls")
        f.write("t")
        f.close()

def youtubeopen(text):
    import urllib.request
    import re
    import webbrowser
    import say

    text2 = text.replace(" ", "+").replace("?", "%3F")

    say.say("odpalam")
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + text2)
    video = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    webbrowser.open("https://www.youtube.com/watch?v=" + video[0])

def setupadd():
    import os
    os.system("@echo off")
    os.system("PyAudio-0.2.11-cp39-cp39-win_amd64.whl")
    os.system("pip install SpeechRecognition")
    os.system("pip install PyAudio")
    os.system("pip install playsound")
    os.system("pip install gTTS")

def play(play):
    import playsound
    playsound.playsound(play)

class Pasek:
    def __init__(self, znak='#', start=0, szerokosc=20, pusto='-'):
        self.znak = znak
        self.start = start
        self.szerokosc = int(szerokosc)
        self.pusto = pusto

    def dalej(self, procent=0):
        linia = "{" + format(round(procent*100, 0), ".0f") + "%}["
        for i in range(self.szerokosc):
            wartosc = i + 1  # 0 + 1 = 1
            aktwartosc = wartosc / self.szerokosc  # 1 / 20 -> 0.05
            if aktwartosc <= procent:
                linia += self.znak
            else:
                linia += self.pusto
        linia += "]"
        print(linia, end="\r")

    def koniec(self):
        self.dalej(procent=1)

# 0.1   0.05 0.1 0.15 0.2
# {10%}[##------------------
def Paseczek(time=0.1):
    from time import sleep
    from os import get_terminal_size

    szerokosc = get_terminal_size()[0]

    pasek = Pasek(szerokosc=szerokosc/2)
    for i in range(50):
        pasek.dalej(procent=i/50)
        sleep(time)
    pasek.koniec()

def cls():
    import os
    os.system("cls")
