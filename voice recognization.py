import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) 

def speak(text):
    """
    Speaks the given text.
    """
    engine.say(text)
    engine.runAndWait()

def get_audio():
    """
    Listens for user input and returns the recognized text.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return None

def respond(text):
    """
    Provides predefined responses based on user input.
    """
    if "hello" in text.lower():
        speak("Hello there!")
    elif "how are you" in text.lower():
        speak("I am doing well, thank you.")
    elif "what time is it" in text.lower():
        now = datetime.datetime.now()
        speak(f"The current time is {now.hour}:{now.minute}.")
    elif "what is the date today" in text.lower():
        today = datetime.date.today()
        speak(f"Today is {today.strftime('%B %d, %Y')}.")
    else:
        speak("I'm still learning. I don't understand that yet.")

def search_web(query):
    """
    Searches the web for the given query.
    """
    webbrowser.open_new_tab(f"https://www.google.com/search?q={query}")
    speak(f"Searching for '{query}' on the web.")

if __name__ == "__main__":
    speak("Hello, I'm ready to assist you.")
    while True:
        user_input = get_audio()
        if user_input:
            respond(user_input)
            if "search" in user_input.lower():
                query = user_input.lower().replace("search ", "")
                search_web(query)