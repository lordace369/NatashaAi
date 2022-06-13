this has a lot of error fixing on mac


Speak() function
. The speak function somehow takes only the string arguments so you have to change your day year and month to string rather than integers before passing them on as arguments to speak()


Speech Recognition
. the port audio fix is attached which is required to install pyaudio and the speech recognition 
. the listening sometimes gets stuck or takes too much time in the integrated terminal but if you run it in the normal terminal of your Mac or Windows then it should fix the problem , if you likely do not have a problem with your microphone.
. another option is to use a timeout and phrase_time_limit property in the "r.listen(source, __ , __) to the seconds you want the listening to stop
