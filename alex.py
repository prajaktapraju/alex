import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import gtts
from time import ctime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def speaking(audioString):
    print(audioString)
    tts = gtts(text = audioString, lang= 'en-in')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning prajakta")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

     
    else:
        speak("Good Evening")

        
    speak("I am sunny dear hope all is well, please tell me what is do for you or how can i help you")   

def takeCommand():
    #It tke microphone input  from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)

        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please")
        return "None"
    return query 
    
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('prajktabagde296@gmail.com', 'praju@123')
    server.sendmail('@gmail.com', to, content)
    server.close()    

if __name__ == "__main__":
    speak("Hello Prajakta Welcome to the AI world")
    wishMe()
    while True:
       query = takeCommand().lower()
       if 'wikipedia' in query:
           speak("searching wikipedia..")
           query = query.replace("wikipedia", "")
           result = wikipedia.summary(query, sentences=6)
           speak("according to wikipedia")
           print(result)
           speak(result)

       elif 'open youtube' in query:
            webbrowser.open("youtube.com")

       elif 'open gmail' in query:
            webbrowser.open("gmail.com")

       elif 'open google' in query:
            webbrowser.open("google.com")

       elif 'the time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"Sir, the time is {strTime}") 

       elif 'open code' in query:
           codePath = "C:\\Users\\prajk\\.vscode " 
           os.startfile(codePath)

       elif 'how are you sunny' in query:
            speak("I am fine how are you")

       elif "where is" in query:
            speak("wait dear")
            query = query.split(" ")
            location = query[2]
            speak("Hold on dear, I will tell you where you are" + location + "is.")
            os.system("chromium-browser  https://www.google.nl/maps/place/" + location + "/&amp;")  
   

       elif 'email to harry' in query:
           try:
                speak("What should I say?")
                content = takeCommand()
                to = "prajktabagde296@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
           except Exception as e:
                # print(e)
                speak("I am not able to send this email")
       
           
