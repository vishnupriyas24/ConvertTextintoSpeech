import os
from gtts import gTTS
def text_to_speech(text, lang='en', slow=False):
    try:
        tts = gTTS(text=text, lang=lang, slow=slow)
        audio_file = "output.mp3"
        tts.save(audio_file)
        print(f"Audio content saved to {audio_file}")
        if os.name == 'nt':  # Windows
            os.system(f'start {audio_file}')
        elif os.name == 'posix':  # macOS and Linux
            os.system(f'afplay {audio_file}')  # macOS
            os.system(f'mpg123 {audio_file}')  # Linux
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    text = "Hello, I am Vishnu Priya. This is my first Project at CodeClause.ThankYou for providing internship!"
    text_to_speech(text)
