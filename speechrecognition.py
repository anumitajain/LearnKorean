
import speech_recognition as sr
import time
# obtain audio from the microphone


def record():
    r = sr.Recognizer()
    ans = ""
    with sr.Microphone() as source:
        #in real code blit "read word" on screen.
        audio = r.listen(source)

    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        splitData = r.recognize_google(audio, language = "ko").lower().split()
        ans += splitData
        time.sleep(5)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

