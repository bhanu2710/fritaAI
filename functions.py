import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import pyautogui
import numpy
import requests
import random
import wikipedia
import pyjokes
import time
import cv2
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import threading
import requests



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
rate = engine.getProperty('rate')                           
engine.setProperty('rate',174)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("good morning!!!")

    elif hour>=12 and hour<10:
        speak("good afternoon!!!")

    else:
        speak("good evening!!!")

    speak("i am friday!!!. Please tell me how may I help you?")

def takecommand(ask = False):
    # it takes microphone input from users and returns string output

    r = sr.Recognizer()
    if ask:
        print(ask)
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language="en-in")
        print("user said:", query)

    except Exception as e:
        return "None"
    return query

def webcam():

    # Load the cascade

    # To capture video from webcam. 
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    # To use a video file as input 
    # cap = cv2.VideoCapture('filename.mp4')

    while True:
        # Read the frame
        _, img = cap.read()

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect the faces

        # Display
        cv2.imshow('img', img)

        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k==27:
            break
            
    # Release the VideoCapture object
    cap.release()


def givenews():
    apiKey = '49e391e7066c4158937096fb5e55fb5d'
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={apiKey}"
    r = requests.get(url)
    data = r.json()
    data = data["articles"]
    flag = True
    count = 0
    for items in data:
        count += 1
        if count > 5:
            break
        print(items["title"])
        to_speak = items["title"].split(" - ")[0]
        if flag:
            speak("Today's top ten Headline are : ")
            flag = False
        else:
            speak("Next news :")
        speak(to_speak)
