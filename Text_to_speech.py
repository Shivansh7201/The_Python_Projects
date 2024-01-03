import pyttsx3

def text_to_speech(text, rate=200):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

# Example usage
text_to_speech("Hello, I am a text to speech bot.")
text_to_speech("I can read any text you want me to read. Just pass it as an argument to the function.")
text_to_speech("I can also read text at different speeds. Just pass the speed as a second argument to the function.",200)
text_to_speech("Now I will explain you how this works. I am using a library called pyttsx3. It is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.",200)
text_to_speech("Thank you for listening.")

