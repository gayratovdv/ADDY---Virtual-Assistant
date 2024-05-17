import pyttsx3
import speech_recognition as sr
import openai


def initialize_tts_engine():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)
    return engine

tts_engine = initialize_tts_engine()

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()
    
    
def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    mic =     sr.Microphone()
    
    with mic as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        response = recognizer.recognize_google(audio)
        print(f"User said: {response}")
        return response
    except sr.RequestError:
        print("API unavailable")
    except sr.UnknownValueError:
        print("Unable to recognize speech")
    return None


openai.api_key = 'your-openai-api-key'

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-004",  # Use the appropriate engine
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    print("Jarvis: Online and ready.")
    speak("Jarvis: Online and ready.")
    
    while True:
        user_input = recognize_speech_from_mic()
        if user_input is None:
            continue
        
        if "exit" in user_input.lower():
            print("Jarvis: Shutting down.")
            speak("Jarvis: Shutting down.")
            break;
        
        response = chat_with_gpt(user_input)
        print(f"Jarvis: {response}")
        speak(response)

if __name__ == "__main__":
    main()