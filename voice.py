import speech_recognition as sr
import pyttsx3
import pywhatkit

# create the speech recognition object and the text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# define the speak() function to speak text aloud
def speak(text):
    engine.say(text)
    engine.runAndWait()

# define the listen() function to recognize speech from the microphone
def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Listening...')
        audio = r.listen(source)
        try:
            print('Recognizing...')
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
        except sr.RequestError:
            print('Sorry, I could not connect to the internet.')

# main loop
while True:
    command = listen()
    if command:
        if 'play' in command.lower():
            song = command[5:]
            speak(f'Playing {song}')
            pywhatkit.playonyt(song)
        elif 'search' in command.lower():
            query = command[7:]
            speak(f'Searching for {query}')
            pywhatkit.search(query)
        elif 'time' in command.lower():
            time = pywhatkit.time()
            speak(f'The current time is {time}')
        elif 'stop' in command.lower():
            speak('Goodbye!')
            break