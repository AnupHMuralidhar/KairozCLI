# modes/voice.py

import sys
import os
import time
import speech_recognition as sr
import pyttsx3
from colorama import init, Fore, Style

init(autoreset=True)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.feature_banner import print_feature_banner

from utils.hf_model import query_huggingface

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print(Fore.YELLOW + "🎙️ Speak now...")
        audio = recognizer.listen(source, phrase_time_limit=10)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "[Voice Error] Could not understand your speech."
    except sr.RequestError as e:
        return f"[Voice Error] Recognition error: {e}"



def main():
    print_feature_banner("🎤 KAIROZ: VOICE-ASSISTED CYBER Q&A")

    while True:
        speak("Ask your cybersecurity question.")
        question = listen()
        print(Fore.LIGHTWHITE_EX + f"\n❓ You said: {question}")

        if "[Voice Error]" in question:
            speak("Sorry, I didn't catch that. Please try again.")
            print(Fore.RED + question)
            continue

        speak("Was that your question?")
        confirm = input(Fore.CYAN + "✅ Was that your question? (y/n): ").strip().lower()

        if confirm != 'y':
            speak("Okay, please repeat your question.")
            question = listen()
            print(Fore.LIGHTWHITE_EX + f"\n❓ You said: {question}")

        speak("Analyzing your question...")
        print(Fore.CYAN + "\n🧠 Thinking with Granite model...\n")
        start = time.time()
        answer = query_huggingface(question)
        duration = round(time.time() - start, 2)

        print(Fore.GREEN + "\n📘 Answer:\n" + "-" * 50)
        print(Fore.LIGHTWHITE_EX + answer.strip())
        print(Fore.BLUE + f"\n⏱️ Completed in {duration} seconds")

        choice = input(Fore.CYAN + "\n🔈 Read the answer aloud? (y/n): ").strip().lower()
        if choice == 'y':
            speak(answer)

        another = input(Fore.CYAN + "\n❓ Ask another question? (y/n): ").strip().lower()
        if another != 'y':
            speak("Thank you. Stay secure!")
            print(Fore.MAGENTA + "\n👋 Exiting voice assistant.")
            break

if __name__ == "__main__":
    main()
