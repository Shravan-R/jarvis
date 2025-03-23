import pyttsx3
import datetime
import pygame
import os

engine = pyttsx3.init("sapi5")
engine.setProperty("rate",200)

def speak(text):
    voice = "en-GB-MaisieNeural"
    command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "output.mp3"'

    os.system(command)
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load("output.mp3")

        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    
    except Exception as e:
        print(e)

    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

def greetMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning,sir")
    elif hour >12 and hour<=18:
        speak("Good Afternoon ,sir")

    else:
        speak("Good Evening,sir")

    speak("Please tell me, How can I help you ?")