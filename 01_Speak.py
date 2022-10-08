import pyttsx3                  
import datetime

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
    speak("I am Derek Hale. How can I help You?")


if __name__=="__main__":
    WishMe()

