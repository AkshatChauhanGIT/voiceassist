import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pyautogui
from pyautogui import click,hotkey
from time import sleep

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak('Good Morning!')

    elif hour>=12 and hour<18:
        speak('Good Afternoon!')

    else:
        speak('Night Sir')
    speak('I am Shadow sir! . How can i help you?')    

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
     #   print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
      #  print("Recognising...")
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")

    except Exception as e:
        #speak('say that again please')
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('teslawrk12@gmail.com', 'llamaloot')
    server.sendmail('teslawrk12@gmail.com', to, content)
    server.close()               


if __name__ == '__main__':
    wishMe() 
    
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia')
            query= query.replace('wikipedia',"")
            results=wikipedia.summary(query,sentences=2)
          # print(results)
            speak("According to wikipedia")
            speak(results)  

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif "on youtube" in query:
            search = query.replace("on youtube", " ")
            print("Searching YouTube...")
            speak("Searching that on YouTube")
            webbrowser.open(f"youtube.com/results?search_query={search}")


        elif 'open google' in query:
            webbrowser.open("google.com") 


        elif 'play music' in query:
            music_dir ='A:\\music'
            songs= os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'open code' in query:
            codePath= "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)        
        
        elif 'downloads' in query:
            cpath= "C:\\Users\\HP\\Downloads"
            os.startfile(cpath) 

      
        elif "shutdown" in query:
            print("Shuting Down...")
            speak("Ok, see you soon")
            exit() 

        elif "toggle bluetooth" in query:
            sleep(2)
            pyautogui.click(x=1714, y=1048)
            sleep(2)
            pyautogui.click(x=1664, y=439)


        





