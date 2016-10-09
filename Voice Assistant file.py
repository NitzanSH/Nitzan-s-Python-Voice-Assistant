import speech_recognition
import os
import webbrowser

recognizer = speech_recognition.Recognizer()


# Contains the actual doing of the command given from the user.
class user_commands:
    def __init__(self):
        pass

    @staticmethod
    def open_browser(browserCommand):
        webbrowser.open("www.google.com", 1, True)
        pass
        print browserCommand


# Listens to user and waits for his command, passes it along
def listen():
    with speech_recognition.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio)

    except speech_recognition.UnknownValueError:
        print("Could not understand audio")
    except speech_recognition.RequestError as e:
        print("Recognition Error; {0}".format(e))

    return ""


# Checks which command it is, calling the correct user_commands method to perform the command
def command(user_phrase):
    uc = user_commands()
    if user_phrase.lower() == 'open google':
        user_commands.open_browser(user_phrase)
    return user_phrase


def main():
    phrase = listen()
    print phrase
    print command(phrase)


if __name__ == '__main__':
    main()
