from sys import path
import pyttsx3       
import speech_recognition as sr               
import datetime
import wikipedia 
import webbrowser
import os
from playsound import playsound
import random



engine = pyttsx3.init('sapi5')        # sapi5 inbuilt voice function by microsoft
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[1].id)

 
def speak(audio):                     #Speak function to speak anything
    engine.say(audio)
    engine.runAndWait()


def WishMe():                          #WishMe Function to Greet 
    hour = int(datetime.datetime.now().hour)    
    if hour>0 and hour>5:
        speak("Good Morning Mihir Sir!")
    elif hour>6 and hour>12:
        speak("Good Afternoon Mihir Sir!")
    elif hour>13 and hour>16:
        speak("Good Evening Mihir Sir!")
    else:
        speak("Good Night Mihir Sir!")
    speak("I am Peter Parker. How can I help You?")


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("Listening...")
        #speak("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
 
    try:
        print("Recognizing...")    
        #speak("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        #speak(query)
        print(f"You Said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        speak("Say that again please...")
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query
 

if __name__=="__main__":

    WishMe()
    while True:
        query = takeCommand().lower()
       
        #logic for executing tasks based on query
        
        #Searching on Wikipedia:---------------------->

        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia","")
            results =  wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)


        #Talking to Program:-------------------------------->

        elif 'how are you' in query:
            speak("I am Fine Sir! what about you")    

        elif 'hello peter' in query:
            speak("Hello Sir How may I Help you")

        elif 'gu kha le' in query:
            speak("Tu kha b s d k")

        elif 'mere babu ne khana khaya' in query:
            speak("Nahi degi wo b s d k soja")

        # elif 'play Dekha Ek Khwaab' in query:
        #    playsound("D:\\main\\My music\\01 DEKHA EK KHAWAB TO.mp3")

        # Performing Tasks:--------------------------------------->
        #Opening Websties:----->

        elif 'open youtube' in query:
            speak("Opening Youtube...")
            speak("sir,what should I search on youtube")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open("www.google.com")

        elif 'open instagram' in query:
            speak("Opening Instagram...")
            webbrowser.open("www.instagram.com")

        elif 'open udemy' in query:
            speak("Opening Udemy...")
            webbrowser.open("udemy.in")

        elif 'wish me again' in query:
            WishMe()
        
        #For Shutdown and Sleep:----------->

        elif 'sleep mode' in query:
            speak("Sleeping...")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        
        elif 'shut down' in query:
            speak("Shutting Down Bye Bye....")
            os.system("shutdown /s /t 1")

        #Opening Applications and System Folders:-------------->

        elif 'open chrome' in query:
            code2 = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            speak("Opening Chrome...")
            os.startfile(code2)

        elif 'open harsh birthday photos' in query:
            photos = "E:\\Harsh Bday"
            speak("Opening Harsh Photos...")
            os.startfile(photos)

        elif 'open vs code' in query:
            codePath = "C:\\Users\\intel\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Opening VS code...")
            os.startfile(codePath)

        elif 'open Java code' in query:
            path = "C:\\Users\\intel\\IntelliJ\\IntelliJ IDEA Community Edition 2021.2.2\\bin\\idea64.exe"
            speak("Opening Java Code...")
            os.startfile(path)
        
        # Playing Music :----------->

        elif 'play music' in query:
            music_dir = 'D:\\main\\new'  
            songs = os.listdir(music_dir)
            #print(songs)
            music = random.choice(songs)
            speak("Playing Music...")
            os.startfile(os.path.join(music_dir,music))
        
        #Asking Time :--------->

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

#def sendEmail(to, content):
    
#dictionary bana ke key me name or words me email add 
#        elif 'email to harry' in query:
#            try:
#                speak("What should I say")
#                content = takeCommand()
#                to = "mihirchouhan22222@gmail.com"
#                sendEmail(to,content)
#                speak("Email has been sent!")
#            except Exception as e:
#                print(e)
#                speak("Sorry!!!") 
