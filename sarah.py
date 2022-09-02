import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import time
import webbrowser
import os
from requests import get
import pywhatkit as kit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(command):
    engine.say(command)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio)
        print(f'User said:  {query}')

    except Exception as e:
        print('Say again please!')
        return listen()    

    return query

def searchBrowser(command):
    webbrowser.open(f'{command}')

def openApp(command):
    os.startfile(command)

def printAndSpeak(command):
    print(command)
    speak(command)


printAndSpeak("Welcome Sir!\nI'm Sarah.")

while True:
    query = listen().lower()

    if 'quit' in query:
        printAndSpeak('Hope See you soon, Sir')
        quit()

    elif 'wikipedia' in query:
        speak('Searching wikipedia...')
        query = query.replace('wikipedia', '')
        results = wikipedia.summary(query, sentences=2)
        printAndSpeak(f'According to wikipedia, {results}')

    elif 'open youtube' in query:
        searchBrowser('youtube.com')

    elif 'open facebook' in query:
        searchBrowser('facebook.com')

    elif 'open google' in query:
        printAndSpeak('what should I search on google')
        query = listen().lower()
        printAndSpeak('searching...')
        searchBrowser(query)


    elif 'open stack' in query:
        searchBrowser('stackoverflow.com')

    elif 'open github' in query:
        searchBrowser('github.com')

    elif 'open wikipedia' in query:
        searchBrowser('wikipedia.com')

    elif 'play music' in query:
        music_dir = 'D:\\Songs\\Hindi'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'tell me the time' in query:
        strTime = datetime.datetime.now().strftime('%H:%M:%S AM')
        printAndSpeak(f"Sir It's {strTime}")

    elif 'open code' in query:
        openApp("C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

    elif 'open cmd' in query:
       os.system('start cmd')

    elif 'open control panel' in query:
       os.system('start control Panel')

    elif 'open chrome' in query:
        openApp("C:\Program Files\Google\Chrome\Application\chrome.exe")

    elif 'open word' in query:
        openApp("C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE")

    elif 'who are you' in query:
        printAndSpeak("I'm sarah, your personal assistant")
        
    elif 'who made you' in query:
        printAndSpeak("I'm designed and created by Zaryab Daha,")

    elif "what's your date of birth" in query:
        printAndSpeak('18 February 2022')

    elif "how are you" in query:
        printAndSpeak("I'm fine, What about you?")

    elif "what are you doing" in query:
        printAndSpeak("Nothing much")

    elif 'my ip' in query:
        ip = get('https://api.ipify.org').text
        printAndSpeak(f'Your IP adress is {ip}')

    # elif 'send message' in query:
        # kit.sendwhatmsg('number', 'message here', 2,22(time))

    elif 'music on youtube' in query:
        printAndSpeak('which song you want to listen')
        query = listen().lower()
        kit.playonyt(query)

    elif 'what can you do' in query:
        printAndSpeak("I can do everthing for you, except those things that I can't, hahaha")

    else:
        pass
        # printAndSpeak('okay Sir')