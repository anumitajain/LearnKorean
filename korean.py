# Korean speaking app
##import codecs
##f1 = codecs.open(file1, "r","utf-8")
##text = f1.read()
##print(type(text))
##print(text.encode('utf-8'))
#----------------------------------------------------------
# convert speech to text

import SpeechRecognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

#-----------------------------------------------------------
# speech to text example from
# https://stackoverflow.com/questions/40549198/text-editor-which-can-convert-speech-to-text-and-vice-versa?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
from SpeechRecognition import * 
from pyttsx import * 

speech_engine = pyttsx.init('sapi5') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
speech_engine.setProperty('rate', 150)

def speak(text):
    speech_engine.say(text)
    speech_engine.runAndWait()

recognizer = SpeechRecognition.Recognizer()

def listen():
    with SpeechRecognition.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_sphinx(audio)
        # or: return recognizer.recognize_google(audio)
    except SpeechRecognition.UnknownValueError:
        print("Could not understand audio")
    except SpeechRecognition.RequestError as e:
        print("Recog Error; {0}".format(e))

    return ""

speak("Say something!")
speak("I heard you say " + listen())



