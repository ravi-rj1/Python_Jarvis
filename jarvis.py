import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")   

    else:
        speak("Good Evening Sir!")  

    speak("I am Jarvis.Ready to take command.")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open whether' in query:
            webbrowser.open("https://weather.com/en-IN/weather/today/l/25.25,87.34?par=google")

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")

        elif 'open stack overflow' in query:
            webbrowser.open("https://stackoverflow.com/")

        elif 'open amazon' in query:
            webbrowser.open("https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_2kclp8mbdm_e&adgrpid=61666692631&hvpone=&hvptwo=&hvadid=486447282128&hvpos=&hvnetw=g&hvrand=7983162009183780440&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9299577&hvtargid=kwd-298441375121&hydadcr=14450_2154367&gclid=CjwKCAiAnO2MBhApEiwA8q0HYQ5DaNsP5DIgC2SwxFSX25QeH_VXrRhzUGv2vcp2tZDqZ8L_OkswqhoCJFEQAvD_BwE") 

        elif 'open microsoft word' in query:
            webbrowser.open("https://www.office.com/launch/word?auth=1")

        elif 'open microsoft powerpoint' in query:
            webbrowser.open("https://www.office.com/launch/powerpoint?auth=1")  
        
        elif 'open vtop vit bhopal' in query:
            webbrowser.open("https://vtop.vitbhopal.ac.in/vtop/initialProcess")
        

        # Accessing local files by using voice command
        elif 'play music' in query:
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play taaja khabar season two episode 1' in query:
            taaja_khabar_season_two_dir = 'D:\\Movie\\Taza_Khabar\\[AllMoviesHub.codes]-taaja.Khabar.S02E01.Hisaab.1080p.WEB-DL.Hindi.DDP5.1.Atmos.H.264.mkv'
            taaja_khabar_season_two = os.listdir(taaja_khabar_season_two_dir)
            print(taaja_khabar_season_two)
            os.startfile(os.path.join(taaja_khabar_season_two_dir,taaja_khabar_season_two[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\ravir\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open python' in query:
            codePath = "C:\\Users\\ravir\\AppData\\Local\\Programs\\Python\\Python310\\python.exe"
            os.startfile(codePath)
        
        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ravirj0110@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir,I am unable to send this mail. Can i try again?")    
