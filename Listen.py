import speech_recognition as sr


def listen():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening.......')
        r.pause_threshold=1
        audio=r.listen(source,0,2)

    try:
        print('Recognising......')
        querry=r.recognize_google(audio,language="en-in")
        print(f"You said : {querry}")
    except:
        return ''
    querry=str(querry)
    return querry.lower()
listen()