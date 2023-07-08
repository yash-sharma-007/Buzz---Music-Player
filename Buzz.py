from gtts import gTTS
import pyttsx3 as pt
import speech_recognition as sr
from playsound import playsound
from datetime import datetime
import time
from pygame import mixer as m
import colorama
from colorama import Fore as p
import sys


# text to speech converter
text_speech = pt.init()
voices = text_speech.getProperty('voices')
text_speech.setProperty('voice', voices[1].id)


def talk(text):
    rate = text_speech.getProperty('rate')
    volume = text_speech.getProperty('volume')
    text_speech.setProperty('rate', 270)
    text_speech.setProperty('voice', voices[1].id)
    rate = 120
    tts = gTTS(text=text, lang='en')
    text_speech.say(text)
    print(text)
    text_speech.runAndWait()


def listen_speech():
    with sr.Microphone() as mic:
        odo = r.listen(mic)
        txt = r.recognize_google(odo)
    return txt


def add_song(s):
    with open("songs.txt", 'a') as f:
        f.write(s+"\n")


def play_song(sng):
    s = f"D:\\SEM 4\\PSC INNOVATIVE\\songs\\{sng}.mp3"
    m.init()
    m.music.load(s)
    m.music.set_volume(0.7)
    m.music.play()
    ans = 'y'
    while ans != 'n':

        print(p.GREEN + "Press 'p' to pause, 'r' to resume ,'e' to exit the program , 'f' for add to favourites")
        query = input("  ")

        if query == 'p':
            # Pausing the music
            m.music.pause()
        elif query == 'r':
            # Resuming the music
            m.music.unpause()
        elif query == 'e':
            # Stop the mixer
            m.music.stop()
            ans = 'n'
        elif query == 'f':
            print(sng, "Added to favourite...")
            with open("favourites.txt", 'a') as f:
                f.write(sng+"\n")

    print("Exit...")




def history(sng):
    with open("history.txt", 'a') as f:
        f.write(sng+",\t\t\t\t")
        print(end="")
        current_time = datetime.now().strftime('%m/%d/%y %I:%M %p')
        f.write(f"{ current_time } \n")


def previous_song():
    with open("history.txt") as f:
        lines = f.readlines()
        i = 0
        s1 = ""
        for line in lines:
            i = i + 1
            if i == len(lines)-1:
                s = line.split(',')
                s1 = s[0]

        print(s1, " is playing...")
        play_song(s1)

# ---------
# speech to text converter


r = sr.Recognizer()
ans = 'yes'
while ans != 'no':
    print(p.CYAN)
    # talk("Welcome to The buzz-music player ")
    # talk("Option 1 : add a new song ")
    # talk("Option 2 : Play a song ")
    # talk("option 3: go to previous song")
    # talk("option 4: add song to favourite")
    # talk("option 5:quit")
    print(p.WHITE)
    talk("Which option you want to choose :")
    audio = listen_speech()
    print(audio)
    if audio == "option 1":
        talk("Which song do you want to add ? ")
        song = listen_speech()
        add_song(song)
        talk(song+" added in your playlist.")
    elif audio == "option 2":
        talk("Which song do you want to listen ? ")
        song_name = listen_speech()
        talk(song_name+" is playing...")
        history(song_name)
        play_song(song_name)
    elif audio == "option 3":
        previous_song()
    elif audio == "option 4":
        pass
    elif audio == "option 5":
        exit()
    else:
        talk("sorry")
    talk("Do you want to continues ? ('yes'/'no')")
    ans = listen_speech()









