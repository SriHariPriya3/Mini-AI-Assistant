import pyttsx3
import speech_recognition as sr
from datetime import datetime
import pywhatkit
import pyjokes
import os

print("Running file:", os.path.abspath(__file__))

# Initialize Text-to-Speech
engine = pyttsx3.init()
engine.setProperty("rate", 170)

voices = engine.getProperty("voices")
if len(voices) > 1:
    engine.setProperty("voice", voices[1].id)


# Speak Function
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


# Listen Function
def take_command():
    recognizer = sr.Recognizer()

    recognizer.energy_threshold = 300
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 1
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)

            print("Recognizing...")
            command = recognizer.recognize_google(audio, language="en-IN")

            print("You said:", command)
            return command.lower()

        except sr.WaitTimeoutError:
            speak("I didn't hear anything.")
            return ""

        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand.")
            return ""

        except sr.RequestError:
            speak("Please check your internet connection.")
            return ""

        except Exception as e:
            print(e)
            return ""


# Main Program
if __name__ == "__main__":

    speak("Hello! I am your AI Assistant.")

    while True:

        command = take_command()

        if command == "":
            continue

        # Time
        elif "time" in command:
            current_time = datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")

        # Date
        elif "date" in command:
            today = datetime.now().strftime("%d %B %Y")
            speak(f"Today's date is {today}")

        # YouTube
        elif "youtube" in command or "play" in command:
            speak("What should I play?")
            song = take_command()

            if song:
                speak(f"Playing {song} on YouTube")
                pywhatkit.playonyt(song)

        # Joke
        elif "joke" in command:
            joke = pyjokes.get_joke()
            speak(joke)

        # Exit
        elif "exit" in command or "bye" in command or "goodbye" in command:
            speak("Goodbye! Have a wonderful day.")
            break

        # Unknown Command
        else:
            speak("Sorry, I don't know this command yet.")