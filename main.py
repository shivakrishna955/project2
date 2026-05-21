from assistant import listen
from voice import speak
from chatbot import ask_ai
from automation import *

# Start message
speak("Jarvis online")

# Main loop
while True:

    query = listen()

    # Skip if nothing recognized
    if query == "":
        continue

    print("You said:", query)

    # Greetings
    if "hi" in query or "hello" in query:
        speak("Hello Shiva")

    # How are you
    elif "how are you" in query:
        speak("I am fine Shiva")

    # Name
    elif "your name" in query:
        speak("I am Jarvis")

    # Open YouTube
    elif "youtube" in query:
        speak("Opening YouTube")
        open_youtube()

    # Screenshot
    elif "screenshot" in query:
        speak("Taking screenshot")
        take_screenshot()

    # Open Notepad
    elif "notepad" in query:
        speak("Opening Notepad")
        open_notepad()

    # Exit program
    elif "exit" in query or "stop" in query:
        speak("Goodbye Shiva")
        break

    # AI Chat
    else:
        try:
            response = ask_ai(query)
            print("AI:", response)
            speak(response)

        except Exception as e:
            print("Error:", e)
            speak("Sorry Shiva, AI service is not working right now")