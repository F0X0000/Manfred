def setup():
    import os
    r = ["t"]
    f = open("install.txt", "r+")
    fr = f.read(1)
    if fr in r:
        print(" ")
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

    say.say("odpalam")
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + text)
    video = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    webbrowser.open("https://www.youtube.com/watch?v=" + video[0])

def setupadd():
    import os
    os.system("PyAudio-0.2.11-cp39-cp39-win_amd64.whl")
    os.system("pip install SpeechRecognition")
    os.system("pip install PyAudio")
    os.system("pip install playsound")
    os.system("pip install gTTS")
    os.system("cls")
