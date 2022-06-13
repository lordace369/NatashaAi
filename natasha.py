import pywhatkit
import webbrowser
import wikipedia
import pyttsx3
import pyjokes
import speech_recognition as sr
from datetime import datetime

# browser=webbrowser.get('chrome')
browser=webbrowser.get('safari')

engine=pyttsx3.init()
# setting the voice for the engine
a=engine.getProperty('voices')
engine.setProperty('voice',a[33].id)

# creating a speak function 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# speak('hey 1')
#tell time
def time():
    t=datetime.now().strftime("%I:%M %p")
    speak(t)
# speak('hey 2')

#tell date
def date():
    day=str(datetime.now().day)
    month=str(datetime.now().month)
    year=str(datetime.now().year)
    date=f'{day},{month},{year}'
    speak(date)
    # speak(day)
    # speak(month)
    # speak(year)

def wishMe():
    hour=int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak(f'Good Morning. It is {hour} o clock ')
    elif hour>=12 and hour<18:
        speak(f'Good Afternoon. It is {hour} o clock ')
    elif hour>=18 and hour<24:
        speak(f'Good Evening. It is {hour} o clock ')
    speak('My name is Natasha. Use "natasha" followed by a command so I can help you.')

# wishMe()
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold=0.8
        r.energy_threshold=300
        # audio=r.listen(source,timeout=6,phrase_time_limit=6)
        audio=r.listen(source)
    try:
        print('recognizing...')
        query=r.recognize_google(audio,language='en-in').lower()

    except Exception as e:
        print(e)
        return 'none'
    return query

# def runAlexa():
#     command=takeCommand()
#     if 'alexa' in command:
#         command=command.replace('alexa','')
#         print(f'you saiid: {command}')
#         if 'play' in command:
#             song=command.replace('play','')
#             print(song)
#             speak(f'playing music {song}')
#             print('playing')
#             pywhatkit.playonyt(song)

#         elif 'time' in command:
#             time()
#         elif 'search about' in command:
#             command=command.replace('search about','')
#             info=wikipedia.summary(command,2)
#             print(info)
#             speak(info)
#         elif 'joke' in command:
#             j=pyjokes.get_joke()
#             print(j)
#             speak(j)
#             # joke=pyjokes.get_joke()
#         elif 'quit' in command:
#             break

#         else:
#             print(command)


#     else:
#         print('try saying alexa in your command')


wishMe()
while True:
    command=takeCommand()
    if 'natasha' in command:
        command=command.replace('natasha','')
        print(f'you saiid: {command}')
        if 'play' in command:
            song=command.replace('play','')
            print(song)
            speak(f'playing music {song}')
            print('playing')
            pywhatkit.playonyt(song)

        elif 'time' in command:
            time()
        elif 'search about' in command:
            command=command.replace('search about','')
            info=wikipedia.summary(command,2)
            print(info)
            speak(info)
        elif 'joke' in command:
            j=pyjokes.get_joke()
            print(j)
            speak(j)
            # joke=pyjokes.get_joke()

        elif 'open' and '.com' in command:
            command=command.replace('open','')
            command=command.replace('.com','')
            speak(f'opening {command}')
            browser.open(f'{command}.com')

        
        elif 'search' and 'on amazon' in command:
            command=command.replace('search','')
            command='+'.join(command.replace('on amazon','').strip().split(' '))
            browser.open(f'http://www.amazon.com/s?url=search-alias%3Daps&field-keywords={command}')

        elif "what can you do" in command:
            speak('Well I can do a lot. You can ask me the time, play something on youtube, open a website and you can ask me for a joke')




        elif 'quit' in command:
            speak("Have a great life master.")
            break

        else:
            print('say \"Natasha quit\" to exit the assistant')


    elif 'quit' in command:
        speak("Have a great life master.")
        break
    
    else:
        print('try saying Natasha in your command or "quit" to exit')
    # runAlexa()