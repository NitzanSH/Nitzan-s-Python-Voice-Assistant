import speech_recognition
import webbrowser
import pyttsx
from pyttsx import voice
import win32api
from threading import Thread
import mtranslate

recognizer = speech_recognition.Recognizer()


# Contains the actual doing of the command given from the user.
class user_commands:
    def __init__(self):
        pass

    @staticmethod
    def open_browser(browserCommand):
        speak("Opening google")
        webbrowser.open("www.google.com", 1, True)
        pass
        print browserCommand

    @staticmethod
    def play_game(gameCommand):
        speak("Have fun playing")
        win32api.ShellExecute(0, 'open', 'Isaac.exe', None, 'D:\Steam\steamapps\common\The Binding Of Isaac', 1)
        pass
        print gameCommand

    @staticmethod
    def translate(translateCommand):
        words = str(translateCommand).split()
        to_text = ''
        for word in words[3:]:
            if word == 'in':
                break
            else:
                to_text += ' ' + word
        in_index = words.index('in')
        to_text = to_text[1:]
        to_lang = getlangcode(words.__getitem__(in_index + 1))
        print to_text
        print to_lang
        translate(to_lang, to_text)
        pass


# Listens to user and waits for his command, passes it along
def listen():
    with speech_recognition.Microphone() as source:
        speak('Please wait a moment')
        recognizer.adjust_for_ambient_noise(source)
        speak('Ready to listen')
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio)

    except speech_recognition.UnknownValueError:
        print("Could not understand audio")
        speak('Sorry, I could not understand you.')
        return None
    except speech_recognition.RequestError as e:
        print("Recognition Error; {0}".format(e))
        # return recognizer.recognize_sphinx(audio)

    return ""


def speak(text, language='en'):
    speech_engine = pyttsx.init('sapi5', False)
    speech_engine.setProperty('rate', 170)
    #engine_voice = speech_engine.getProperty('voices')
    #engine_voice = engine_voice[:1]
    #final_voice = voice.Voice(engine_voice, [language])
    #speech_engine.setProperty('voice', final_voice.id)
    speech_engine.say(text)
    speech_engine.runAndWait()


def translate(lang, phrase):
    speak(mtranslate.translate(phrase, lang, 'en'))


def getlangcode(language):
    langCodes = {'french': 'fr',
                 'spanish': 'es'
                 }
    return langCodes[language.lower()]


# Checks which command it is, calling the correct user_commands method to perform the command
def command(user_phrase):
    # All the threads will automatically close when the functions in 'user_commands' will return
    thread = None
    if user_phrase is None:
        return ""
    elif user_phrase.lower() == 'open google':
        thread = Thread(target=user_commands.open_browser, args=(user_phrase,))
        thread.start()
    elif user_phrase.lower() == 'play game':
        thread = Thread(target=user_commands.play_game, args=(user_phrase,))
        thread.start()
    elif user_phrase[:10].lower() == 'how to say':
        thread = Thread(target=user_commands.translate, args=(user_phrase,))
        thread.start()
    else:
        speak("That\'s not a command. Please check the available command list.")
    return user_phrase


def main():
    phrase = None
    phrase = listen()
    #phrase = 'how to say i love you in french'
    command(phrase)


if __name__ == '__main__':
    main()
