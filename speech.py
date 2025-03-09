import speech_recognition as sr

def recognize_speech():
    """
    Captures audio from the microphone and converts it to text using Google Web Speech API.
    """
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening... Speak now!")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        print("Recognized Text:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Could not request results, please check your internet connection.")

if __name__ == "__main__":
    recognize_speech()
