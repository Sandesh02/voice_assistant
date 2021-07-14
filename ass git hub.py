import datetime
import os
import webbrowser

import PyPDF2
import pyjokes
import pyttsx3
import random
import speech_recognition as sr
import wikipedia
import wolframalpha

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):  # function for speaking
    engine.say(audio)
    engine.runAndWait()

def welcome():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


r=sr.Recognizer()# initialise a recogniser
# listen for audio and convert it to text:
def takeCommand():
    with sr.Microphone() as source: # microphone as source

        print("listening....")
        audio = r.listen(source, 5, 5)  # listen for the audio via source

        query = ''
        try:

            query = r.recognize_google(audio)  # convert audio to text
            print('Recognizing...')
            print("user said:", query.lower())  # print what user said

        except Exception as e:

            # print(e)

            speak("Say that again please...")

            return "None"

        return query.lower()
if __name__ == "__main__":
    welcome()
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
            speak('opening youtube')
            webbrowser.open("youtube.com")


        elif 'open google' in query:
            speak('opening google')
            webbrowser.open("google.com")


        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open gmail' in query:
            webbrowser.open('gmail.com')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'play music' in query:
            music_dir = 'S:\music'
            songs = os.listdir(music_dir)
            print(songs)
            speak("tell me  the number of song you would like to play")
            a = int(takeCommand())
            os.startfile(os.path.join(music_dir, songs[a]))

        elif 'read a book' in query:
            # path of the PDF file
            path = open("D:\sandesh\FY\SEM1\BXE\sacc\MOSFET.pdf", 'rb')
            pdfReader = PyPDF2.PdfFileReader(path)
            from_page = pdfReader.getPage(1)
            text = from_page.extractText()
            os.startfile("D:\sandesh\FY\SEM1\BXE\sacc\MOSFET.pdf")
            speak(text)


        elif 'who are you' in query:
            speak('My name is Jarvis, I am your personal assistant')

        elif 'what can you do' in query:
            speak(
                'I can do lots of things, for example you can ask me time, date, weather in your city,I can open websites for you,'
                ' i can launch applications and any simple calculations ')

        elif 'how are you' in query:
            li = ['good', 'fine', 'great']
            response = random.choice(li)
            print("I am", response)
            speak("I am {}".format(response))

        elif 'tell me jokes' in query:
            joke = pyjokes.get_joke(language="en", category="all")
            speak('here is a joke')
            print(joke)
            speak(joke)

        elif "don't listen" in query or "stop listening" in query:
            print("okay;i am terminating myself")
            speak("okay;i am terminating myself")
            exit()


        elif 'search' in query:

            indx = query.lower().split().index('search')
            query = query.split()[indx + 1:]
            webbrowser.open("https://www.google.com/search?q ="+str(query))

        elif 'search for' in query:
            search_term = query.replace("search", "")
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            speak("Here is what I found for" + search_term + "on google")

        elif 'open chrome' in query:
            speak('opening,google chrome')
            os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")


        elif 'open powerpoint' in query:
            speak('opening,powerpoint')
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\PowerPoint 2013.lnk')


        elif 'open word' in query:
            speak('opening,word')
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk')
            exit()
        elif 'calculate' or 'plot' in query:
            try:
                app_id = "8QP7W5-RY8P4WE3YQ"
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)
            except Exception as e:
                exit()
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
        else:
            exit()