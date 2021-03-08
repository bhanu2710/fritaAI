from functions import *

def protocols():    
    while True:
        # logic 
        query = takecommand().lower()

        if 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            print(strTime)
            speak(f"sir the time is {strTime}")
                        
        elif 'what is day today' in query:
            strdate = datetime.datetime.now().strftime("%d-%m-%y %H")  
            print(strdate)     
            speak(f"Sir today is{strdate}")

        elif 'who made you' in query:
            speak("It seems to be that a human made me")

        elif 'who are you' in query or 'what is your name' in query:
            speak("I Am Frita. Your Virtual Assistant")

        elif 'hey' in query or 'hi' in query or 'hello' in query or 'whats up' in query:
            speak("Hi sir!")

        elif 'where do you live' in query:
            speak("I lives in heart of your computer")

        elif 'can i change your name' in query:
            speak("sorry sir but I like my name")

        elif 'awesome' in query or 'wow' in query or 'amazing' in query or 'wonderful' in query:
            speak("Thanks for praising me.")

        elif 'do you know alexa' in query or 'is alexa is your friend' in query: 
            speak("Alexa and I are best friend")
        
        elif 'how are you' in query or 'are you ok' in query or 'need any help' in query:
            speak("I am ok, what about you")
        
        elif 'I am ok' in query or 'I am good' in query or 'I am fine' in query:
            speak("Well, that is good to hear.")

        elif 'show my picture' in query:
            webcam()
                

        elif 'see you friday' in query or 'friday quit' in query or 'quit' in query or 'bye' in query:
            speak("OK Sir See You Next Time")
            exit()
            quit()

        # takecommand and deep learning
        
        elif 'search' in query:
            speak("What do you want to search for?")
            search = takecommand("What do you want to search for?")
            url = 'http://www.google.com/search?&q=' + search
            webbrowser.get().open(url)
            speak("Here it is what I found on google")

        elif 'play video' in query or 'channel' in query:
            speak("Which type of video or channel?")
            search = takecommand("Which type of video or channel?")
            url = 'http://www.youtube.com/search?&q=' + search
            webbrowser.get().open(url)
            speak("This is it!!!")  

        elif 'where' in query or 'how' in query or 'what' in query or 'when' in query or 'can you' in query\
        or 'explain' in query or 'who' in query or 'about' in query:
            try:
                speak("Searching in data.")
                session = requests.Session()
                retry = Retry(connect=3, backoff_factor=0.5)
                adapter = HTTPAdapter(max_retries=retry)
                url = "https://www.wikipedia.org"
                session.mount('http://www.wikipedia.org', adapter)
                session.mount('https://www.wikipedia.org', adapter)
                session.get(url)
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("I got it.")
                print(results)
                speak(results)
            except Exception as e:
                speak("Sorry, nothing found in data like this")

        elif 'download song' in query:
            speak("Can you tell the song please?")
            s1 = takecommand("Can you tell the song please?")
            u1 = 'mp3quack.com/search?q=' + s1
            webbrowser.get().open(u1)
            speak("i think this is it")

        elif 'open' in query:
            speak("What should I open in chrome?")
            s2 = takecommand("What should I open in chrome?")
            u2 = webbrowser.open_new_tab(f"http://{s2}.com")
            webbrowser.get()

        elif 'tell me some jokes' in query or 'jokes' in query or 'tell me joke' in query:
            speak("Sure sir")
            jokes = pyjokes.get_joke(language='en', category='neutral')
            print(jokes)
            speak(jokes) 
       

        # commands            

        elif 'open google' in query:
            speak("Of course sir")
            webbrowser.open('http://google.com')

        elif 'open wikipedia' in query:
            webbrowser.open("http://wikipedia.com")    

        elif 'open new tab' in query:
            speak("yes sir")
            webbrowser.open_new_tab('http://google.com')

        elif 'headlines' in query or 'news' in query or 'headline' in query:
            speak("Sure sir.")
            givenews()

        elif 'screenshot' in query:
            speak("Ready!!!")
            speak("Five")
            speak("Four")
            speak("Three")
            speak("Two")
            speak("One")
            img = pyautogui.screenshot() 
            img.save("Screenshot.jpg")
            speak("Screenshot taken")       

        elif 'wait a minute' in query or 'wait a minute please' in query: 
            speak("Ok sir , meet you after 10 seconds")
            time.sleep(10)
            speak("I am back sir ,can we start now.")  
        
        elif 'play a song' in query or 'play song' in query:
            speak("which song do you want to play?")
            song = takecommand("Which song do you want to play?")
            u10 = webbrowser.open_new_tab(f"https://gaana.com/song/" + song)



        # hotstar    

        elif 'open hotstar' in query:
            speak("sure sir")
            webbrowser.open_new_tab('http://hotstar.com/in')

        elif 'open marvel movies' in query:
            speak("sure sir")
            webbrowser.open_new_tab('https://www.hotstar.com/in/channels/marvel')            

        elif 'play latest episode of anupama' in query or 'anupama' in query:
            speak("of course sir")
            webbrowser.open_new_tab("https://www.hotstar.com/in/tv/anupamaa/1260022017")

        # prime video
        elif 'open prime' in query:
            speak("sure sir")
            webbrowser.open_new_tab('http://primevideo.com')    

        # differents            

        elif 'open flipkart' in query:
            speak("of course sir")
            webbrowser.open_new_tab("http://flipkart.com")    

        elif 'open whatsapp' in query:
            speak("sure sir")
            webbrowser.open_new_tab("http://web.whatsapp.com")               

        elif 'open youtube' in query:
            speak("sure sir")
            webbrowser.open_new_tab('http://youtube.com')              

        # locations                                   

        elif 'open team viewer' in query:
            speak("sure sir")
            codepath = "C:\\Program Files (x86)\\TeamViewer\\TeamViewer.exe"
            os.startfile(codepath)        

        elif 'open new window' in query:
            speak("wait a minute")
            codepath = "C:\\Users\\ASHOK\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codepath)      

        elif 'open any desk' in query:
            speak("yes sir")
            codepath = "C:\\Program Files (x86)\\AnyDesk\\AnyDesk.exe"
            os.startfile(codepath)    

        elif 'open chrome' in query:
            speak("sure sir")
            codepath = "C:\\Users\\ASHOK\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codepath)    
