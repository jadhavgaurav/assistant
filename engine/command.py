import pyttsx3
import speech_recognition as sr

import time

import eel

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) 
    engine.setProperty('rate', 165)
    eel.DisplayMessage(text)
    # print(voices)
    engine.say(text)
    engine.runAndWait()
    


def takeCommand():
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening.....")
        eel.DisplayMessage("Listening.....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)
        
    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        eel.DisplayMessage(query)
        # time.sleep(2)
        # speak(query)
        
    
    except Exception as e:
        return ""
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    return query.lower()


@eel.expose
def allCommands():
    
    try:
        query = takeCommand()
        print(query)
        
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)
            
        # create whatsapp command

        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp
            flag = ""
            contact_no, name = findContact(query)
            if(contact_no != 0):

                if "send message" in query:
                    flag = 'message'
                    speak("what message to send")
                    query = takeCommand()
                    
                elif "phone call" in query:
                    flag = 'call'
                else:
                    flag = 'video call'
                    
                whatsApp(contact_no, query, flag, name)

        
    except:
        print("Error")
        
    
    eel.ShowHood()