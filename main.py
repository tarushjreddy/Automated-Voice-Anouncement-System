
from gtts import gTTS
from pydub import AudioSegment
import pandas as pd
import os


def ttos(text, filename):
    pass


def mergeaudio(audios):
    pass


def generateSkelton():
    audio = AudioSegment.from_mp3('Announcement Sound Effects All Sounds.mp3')
    # 1
    start = 0
    end = 10000
    audioProcessed = audio[start:end]
    audioProcessed.export("1_hindi.mp3", format="mp3")
    # 2 from address
    # 3 via address
    # 4 to  address


def GenerateAnounce(filename):
    pass


if __name__ == "__main__":
    print("omsai")
    generateSkelton()
    print("Now generating anouncement")
    GenerateAnounce("announce.xlsx")
