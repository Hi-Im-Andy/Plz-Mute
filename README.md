# Plz-Mute
This is used to stop discourage people from being loud.

## Why?
The purpose of this script is to discourage people (Like my loud roomate) from making noise while playing games, watching sports, etc.

## Setup
Setting this up requires the code to be compatable on the users computer, so their permission is needed. **DO NOT** use this on someone elses property without their consent.

Libraries needed:
+ pyaudio (pip install pyaudio)
+ numpy (pip install numpy)
+ audioop (pip install numpy)
+ time
+ os

There might be some trouble obtaining pyaudio with python3. The best fix for windows is to open CMD and enter the following:
+pip install pipwin
+pipwin install pyaudio

This should be all for the initial setup. 

## Running the Code
It is importatnt to know what program needs to be closed beforehand. Using my roommate as an example, he yells an obsurd amount when playing League of Legends. So for this, the desired app to be closed is League of legends.

Similarly, it is important to know the noise tolerance. The average conversation is 60dB while a motorcycle engine is 95dB. That being said, I have it set to stop my roommate from being too loud, so the cutoff was around 85dB.
