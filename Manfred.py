###########################Manfred##############################################
from skript import *
############################install#############################################
setup()

import os
from audio import get_audio
from gtts import gTTS
import speech_recognition as sr
import playsound
import time
import sys
import random
from say import  *
from logo import logo
from time import sleep
from pogoda import *
from czy import *
import webbrowser

################################################################################

logo()
say("Witaj, Jestem Manfred")

################################################################################

yt = ["youtube", "youtubie", "film"]
ADMIN_COMMADN = ["admin"]
PA_ADMIN = ["pa", "pa pa", "papa"]
RESTART_ADMIN = ["restart"]
KLUCZ_COMMAND = ["ok", "manfred", "bot", "okej", "żulu",  "manfredi"]
PROSZE = ["prosze", "proszę"]
odpal = ["odpal"]
google = ["google"]
jaka = ["jaka"]
jest = ["jest"]
setupup = ["setup", "set up"]
temperatura = ["temperatura"]
w = ["w"]
BIAŁYSTOK = ["białymstoku"]
BIELSK = ["bielsk", "bielsko"]
bielskbiałej = ["bielsk-białej", "bielsku-białej"]
BIAŁE = ["białe"]
WARSZAWA = ["warszawie"]
wyszukaj = ["wyszukaj"]

################################################################################

################################################################################

def COMMAND():
    while True:
        print(" ")
        audio = get_audio()
        if audio != None:
            if len(czy(audio, ADMIN_COMMADN)):
                if len(czy(audio, google)):
                    g = audio.lower().split(' ' + czy(audio, google)[0] + ' ')[1]
                    say("Oto co mi się znaleść.")
                    googleurl = "https://www.google.com/search?q=" + g.replace(" ", "+").replace("?", "%3F")
                    webbrowser.open(googleurl)
                if len(czy(audio, PA_ADMIN)):
                    say("pa")
                    quit()
                    exit()
                if len(czy(audio, RESTART_ADMIN)):
                    os.system("cls")
                    os.system("python Manfred.py")
                if len(czy(audio, setupup)):
                    say("ok")
                    setupadd()
            if len(czy(audio, KLUCZ_COMMAND)):
                if len(czy(audio, jaka)):
                    if len(czy(audio, jest)):
                        if len(czy(audio, temperatura)):
                            if len(czy(audio, w)):
                                if len(czy(audio, BIAŁYSTOK)):
                                    temp("Białystok")
                                if len(czy(audio, WARSZAWA)):
                                    temp("Warszawa")
                                if len(czy(audio, bielskbiałej)):
                                    pogo("Bielsko")
                                if len(czy(audio, BIELSK)):
                                    if len(czy(audio, BIAŁE)):
                                        pogo("Bielsko Biała")

                if len(czy(audio, wyszukaj)):
                    g = audio.lower().split(' ' + czy(audio, wyszukaj)[0] + ' ')[1]
                    say("Oto co mi się udało znaleść.")
                    googleurl = "https://www.google.com/search?q=" + g.replace(" ", "+").replace("?", "%3F")
                    webbrowser.open(googleurl)
                if len(czy(audio, odpal)):
                    if len(czy(audio, PROSZE)):
                        if len(czy(audio, yt)):
                            ytw = audio.lower().split(' ' + czy(audio, yt)[0] + ' ')[1]
                            youtubeopen(ytw)

COMMAND()
