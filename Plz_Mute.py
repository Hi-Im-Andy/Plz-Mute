import time
import os
import pyaudio
import audioop
import math

p = pyaudio.pyaudio()
stream = p.open(format = pyaudio.paInt16,
 channels = 1, rate = 44100, input = True, 
 frames_per_buffer = 1024)

while 1:
    data = stream.read(1024)
    rms = audioop.rms(data, 2)
    decibel = 20 * math.log10(rms) #Converts rms to decibels
    if(decibel > 85): #Checks if the sound is louder than 85 decibels
        os.system("TASKKILL /F /IM application.exe") #Kills application