import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+50)
engine.setProperty('voice', voices[-1].id)

def fala(texto):
    print(texto)
    engine.say(texto)

    engine.runAndWait()