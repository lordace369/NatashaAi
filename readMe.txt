This is a voice is assistant made in Python with the help of the following modules :
. pyttsx3 for text to speech
. SpeechRecognition for listening to commands and converting them to text
. pywhatkit for playing videos on youtube
. webbrowser for opening website links on the browser
. datetime module for determining the time
. pyjokes for getting a joke
. wikipedia

This program takes a command if it is followed by the word Natasha
. ask time to know the time : for eg- "Natasha tell me the time"
. ask to play something on youtube : for eg- "Natasha play Linkin Park"
. ask for a joke : for eg- "Natasha tell me a joke"
. ask to open a website with '.com' : for eg- "Natasha open amazon .com "
. ask to search for a product on amazon : for eg- "Natasha SEARCH FOR black boots'
. ask to search about something on wikipedia  : for eg- "Natasha SEARCH ABOUT the universe'

Many features could be added



The program has a lot of error fixing on mac


Speak() function
. The speak function somehow takes only the string arguments so you have to change your day year and month to string rather than integers before passing them on as arguments to speak()


Speech Recognition
. the port audio fix is attached which is required to install pyaudio and the speech recognition 
. the listening sometimes gets stuck or takes too much time in the integrated terminal but if you run it in the normal terminal of your Mac or Windows then it should fix the problem , if you likely do not have a problem with your microphone.
. another option is to use a timeout and phrase_time_limit property in the "r.listen(source, __ , __) to the seconds you want the listening to stop
