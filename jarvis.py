import os
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import smtplib


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
    speak('I am Your assistant sir, Please tell me how may I help you')         

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
        print('Suraj:',query) 
        
    except Exception as e:
       # print(e)
        
        print('Say that again please...') 
        return 'None'
    return query        
        
def sendMail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("misrasuraj11@gmail.com","yourpassword")
    server.sendmail('misrasuraj11@gmail.com',to,content)
    server.close()
    
    
if __name__=="__main__":
    wishMe()
    while True:
        
        query = takeCommand().lower()
        
        #Logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia:")
            print(results)
            speak(results)
         
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 
        elif 'play music' in query:
            music_dir = 'E:\\Suraj\\Favorites'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak('Sir, the time is: ',strTime)
        
        elif 'open code' in query:
                codePath = "C:\\Users\\misra\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)        
                
        elif 'send mail' in query:
            try:
                speak("what should I say...?")
                content = takeCommand()
                to = "sm314310@bbdu.ac.in"
                sendMail(to,content)
                speak("Mail has been sent!")
            except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to send this mail")
        elif 'please stop' in query:
            exit()            
                       
                
                         