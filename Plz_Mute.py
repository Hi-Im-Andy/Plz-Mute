import time
import os
import pyaudio
import audioop
import math
from datetime import date
import playsound
from gtts import gTTS

def last_strike (today):
    day_strike = date.today()
    day_strike = day_strike.strftime("%m-%d-%Y")
    
    if (today == day_strike):
        strikes -= 1
        audio_string = "Frankie! This is a warning! Please Mute" # This is the audio that should be played
        tts = gTTS(text = audio_string, lang="en")
        audio_file = 'audio.mp3'
        tts.save(audio_file)
        playsound.playsound(audio_file)
        os.remove(audio_file) #Deletes the audio file after it is played
    else:
        day_strike = today
        strikes = 3
    if(strikes <= 0):
        return True
    return False

p = pyaudio.PyAudio()
stream = p.open(format = pyaudio.paInt16,
 channels = 1, rate = 44100, input = True, 
 frames_per_buffer = 1024)

while 1:
    today = date.today()
    today = today.strftime("%m-%d-%Y")
    data = stream.read(1024)
    rms = audioop.rms(data, 2)
    print(rms)
    # decibel = math.log10(rms) #Converts rms to decibels
    # if((decibel * 20)> 85): #Checks if the sound is louder than 85 decibels
    #     if(last_strike(today)):
    #         os.system("TASKKILL /F /IM application.exe") #Kills application