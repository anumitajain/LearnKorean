import pyttsx3
engine = pyttsx3.init()
languages = engine.getProperty('languages')
for language in languages:
    engine.setProperty('language', language.id)
    engine.say("my name is bob")
engine.runAndWait()

