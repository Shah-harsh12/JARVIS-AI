import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import openai

import cv2

face_cap = cv2.CascadeClassifier("C:/Users/Harsh/AppData/Roaming/Python/Python311/site-packages/cv2/data/haarcascade_frontalface_default.xml")

video_cap = cv2.VideoCapture(0)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id) #use voice[0] for male voice and voice[1]for femail voice
engine.setProperty('voices' , voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
      speak("Good Evening")
    speak("Hello master harsh. i am jarvis. how may i help you?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=0.2)
        r.pause_threshold = 0.8
        r.energy_threshold = 300 
        print("Listening...")
        audio = r.listen(source , timeout=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language="en-IN")
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)

        print("Say that again please")
        speak("can you please say that again")
        return"none"
    return query



if __name__ == '__main__':
   wishMe()
   while True:
    
     query = takecommand().lower()

     if 'wikipedia' in query:
         speak('searching wikipedia...')
         query = query.replace("wkikipedia", " ")
         result = wikipedia.summary(query,  sentences=1)
         speak('According to wikipedia..')
         print(result)
         speak(result)

     elif 'open youtube' in query:
         webbrowser.open("youtube.com")
         speak("opening youtube")
         print("opening youtube")

     elif 'open google' in query:
         webbrowser.open("google.com")
         speak("opening google")
         print("opening google")
     elif 'open any watch' in query:
         webbrowser.open("https://aniwatch.to/home")
         speak("opening aniwatch")
         print("opening aniwatch")
     elif 'play music' in query:
         music_dir = 'D:\\movies\\music\\workout'
         songs = os.listdir(music_dir)
         print(songs)
         os.startfile(os.path.join(music_dir , songs[0]))
     elif 'the time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"sir , the time is {strTime}")
         print(strTime)
     elif 'open chrome' in query:
         codePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
         os.startfile(codePath)
         speak("opening chrome")
         print("opening chrome")
     elif 'thank u' in query:
         speak("your welcome sir , anything else sir")
     elif 'who made you' in query:
         speak("master shah harsh made me. i am his assistant jarvis. i am programed in python programing language")
     elif 'what can you do' in query:
         speak("i can play music, open selected website and applications , provide any information according to wikipedia")
     elif 'search' in query:
         webbrowser.open(query)
         query = query.replace("search" , " ")
         speak("here is your result")
         print("here is your result")
     elif 'face' in query:
            while True:
                rat , video_data = video_cap.read()
                col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
            
                face = face_cap.detectMultiScale(
                    col,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30,30),
                    flags=cv2.CASCADE_SCALE_IMAGE
                )

                for(x,y,w,h) in face:
                    cv2.rectangle(video_data,(x,h),(x+w,y+h),(0,255,0),2)

                cv2.imshow("video_live", video_data)
                if cv2.waitKey(10) == ord("a") :
                    break
#press a to stop the video
            video_cap.release() 
        
