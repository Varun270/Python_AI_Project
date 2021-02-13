import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

"""Selecting Voice for our speech assistance 
and using sapi5 for reading instructions
"""

engine =pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)

"""
speak function is responsible for our speech recognition system to speak 
"""
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
"""
Wishme is responsible for wishing me
"""
def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Varun")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Varun")
    else:
        speak("Good Evening Varun")

    speak("I am Jarvis .Please tell me how can I help you sir")
"""
It takes microphone input from user and returns string output
"""
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1 # Allows user to take gap while ordering something
        audio = r.listen(source)
    try:
        print("Recognizing......")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said:{query}\n")
    except Exception as e:
        #print(e)
        print("Say that again please ....")
        return "None"
    return query

def sendemail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com","your-password")
    server.sendmail("youremail@gmail.com",to,content)
    server.close()





if __name__ == '__main__':
    WishMe()
    while True:
        query = takeCommand().lower()
        # logic for executing tasks on query
        if "wikipedia" in query:
            speak("Searching wikipedia .....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "open github" in query:
            webbrowser.open("github.com")

        elif "play music " in query:


            music_dir = 'C:\\Users\\Varun Shrivastava\\Documents\\music_dir'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
            

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

        elif "open pycharm " in query:
            code_path = "C:\\Users\\Varun Shrivastava\\Desktop\\PyCharm Community Edition 2020.2.3\\bin\\pycharm64.exe"
            os.startfile(code_path)
        elif "email to Hassan" in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = "HassanyourEmail@gmail.com"
                sendemail(to,content)
                speak("Email has been sent what else can i do for you")
            except Exception as e:
                print(e)
                speak("Sorry my friend Varun bhai i am not able to send this email at this moment")







