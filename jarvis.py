import speech_recognition as sr
import pyttsx3
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak('Good Morning')
    elif hour >=12 and hour <= 17:
        speak('Good Afternoon')  
    else:
        speak('Good Evening') 
    speak('I am Jarvis sir, Please tell me how may I help you')         

def takeCommand():
    #it takes voice input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 2
        audio = r.listen(source)
        
        
    try:
        print('Recognizing...')
        query = r.recognize_google(audio,language='en-in')
        print('User said:',query) 
        
    except Exception as e:
       # print(e)
        
        print('Say that again please...') 
        return 'None'
    return query        
        

if __name__=="__main__":
    wishMe()
    takeCommand()