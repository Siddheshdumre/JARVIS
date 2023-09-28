import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")

    speak("Jarvis here. How may I assist you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Interpreting...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User : {query}\n")
    except Exception as e:
        print("Sorry, I'm unable to recognize. Can you please repeat")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    music_dir = 'C:\\Users\\HP\\Desktop\\SIDDHESH PC\\[SPOTIFY-DOWNLOADER.COM] Is This Love_'
    songs = os.listdir(music_dir)

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
        elif 'search on youtube' in query:
            query = query.replace("search on youtube", "")
            webbrowser.open(
                f"https://www.youtube.com/results?search_query={query}")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
        elif 'search on google' in query:
            query = query.replace("search on google", "")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        elif 'play music' in query:
            random_song = random.choice(songs)
            song_path = os.path.join(music_dir, random_song)
            os.startfile(song_path)
            speak(f"Playing {random_song}")
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
