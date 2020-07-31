import speech_recognition as sr #please put a library into repository
import os
from pydub import AudioSegment
import vk
from random import randint
import time
import requests


def convert_ogg_to_wav(file):
    path = os.getcwd()
    os.chdir("/root/BotRaya/BotRaya/media/")
    dst = file[:-4]+".wav"
    sound = AudioSegment.from_ogg(file)
    sound.export(dst, format="wav")
    file = open(dst, 'rb')
    os.chdir(path)
    return file


def send_message(peer_id, message):
    session = vk.Session(
        access_token="85517bc6c0ed534901b211e166121548886e95e73ffa7656f9a13532c7c270a710c1ab3aa4148bccfdf4b")
    api = vk.API(session, v="5.103")
    api.messages.send(
        random_id=randint(0, 9999),
        peer_id=peer_id,
        message=message
    )
    return 0


def download_ogg(url):
    r = requests.get(url)
    filename = url.split("/")[-1]
    path = os.getcwd()
    os.chdir("/root/BotRaya/BotRaya/media/")
    with open(filename, 'wb') as f:
        f.write(r.content)
    os.chdir(path)
    return filename


def speech_to_text(url, peer_id, start_message):
    start_time = time.time()
    filename = download_ogg(url)
    r = sr.Recognizer()
    dst = convert_ogg_to_wav(filename)
    file = sr.AudioFile(dst)
    with file as source:
        audio = r.record(source)
    return send_message(
        peer_id,
        "{start} {message}\nTime: {time}".format(
            start=start_message,
            message=r.recognize_google(audio, language="ru_RU"),
            time=time.time()-start_time
        )
    )

print(speech_to_text("https://psv4.userapi.com/c205120//u367833544/audiomsg/d10/549fcca9ec.ogg", 147084786, "[shish7]"))