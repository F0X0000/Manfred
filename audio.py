import speech_recognition as sr

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Nasłuchuję...")
        audio = r.listen(source)
        said=""
        try:
            said= r.recognize_google(audio, language="pl")
            print("Powiedziałeś: " + said.lower())
        except Exception as e:
            print("Czekam na komendę..." + str(e))

    return said.lower()
