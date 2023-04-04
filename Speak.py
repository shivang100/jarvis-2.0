import pyttsx3


def say(text):
    engine=pyttsx3.init("sapi5")
    voices=engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)

    engine.setProperty('rate',200)

    print(f"A.I:{text}")
    engine.say(Text=text)
    engine.runAndWait()
    print('    ')