import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import smtplib
import os
import webbrowser
import warnings

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)
chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!')
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am phoebe, your assistant bot. Please tell me how may I help you?")

def command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except Exception as e:
        print(e)
        print("Audio not redable")
        #speak("Can you repeat that?")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def processes():
    greet()
    query=" "
    process=" "
    url=' '
    while 'goodbye phoebe' not in query:
        query=command().lower()
        

        #performing actions
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            process=results
            speak(results)

        elif "how are you? " in query:
            speak("I am fine what about you?")
            process="I am fine what about you?"

        elif 'open youtube' in query:
            webbrowser.get('chrome').open("youtube.com")
            process="Youtube Opened"

        elif 'open google' in query:
            webbrowser.get('chrome').open("google.com")
            process='Google opened'

        elif 'open stackoverflow' in query:
            webbrowser.get('chrome').open("stackoverflow.com")
            process='stackoverflow opened'
        
        elif 'open whatsapp' in query:
            webbrowser.get('chrome').open("web.whatsapp.com")
            process='WhatsApp opened'

        elif 'open facebook' in query:
            webbrowser.get('chrome').open("facebook.com")
            process='FaceBook opened'


        elif 'play music' in query:
            music_dir = 'C:\\Music\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            process='Playing music'

        elif 'search' and 'on youtube' in query:
            search_term = query.split("for")[-1]
            url = "https://www.youtube.com/results?search_query=" + search_term
            webbrowser.get().open(url)
            process="Opening" + search_term 

        elif 'search' in query:
            search_term = query.split("for")[-1]
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            process="Opening" + search_term 


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            process= (f"{strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\itians\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            process='Code opened'


        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = command()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
                process="Email has been sent"
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")
                process="Sorry. I am not able to send this email"  


        else:
            speak('Can you repeat that?')     

    speak("Goodbye! I hope we will meet again soon")
    process='Goodbye! I hope we will meet again soon'


