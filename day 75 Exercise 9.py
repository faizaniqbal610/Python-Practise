import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0])

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

if __name__ == "__main__":

    names = ["Faizan", "Rehan", "Aliyan", "Zohan", "Ali"]
    for name in names:
        speak(f"Shoutout to {name}")

