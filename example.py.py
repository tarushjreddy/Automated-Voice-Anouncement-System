from gtts import gTTS
from pydub import AudioSegment
import pandas as ps
import os
from playsound import playsound
from pydub.playback import play
import xlrd


def textToSpeech(text, filename):
    mytext = str(text)
    language = 'en'
    myobj = gTTS(slow=False, lang=language, text=mytext)
    myobj.save(filename)


def mergeaudio(audios):
    # this is a function used to merge audios
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined


# def generateSkelton():
#     audio = AudioSegment.from_mp3('Announcement Sound Effects All Sounds.mp3')
#     # 1
#     start = 0
#     end = 10000
#     audioProcessed = audio[start:end]
#     audioProcessed.export("1_hindi.mp3", format="mp3")
#     # 2 from address
#     # 3 via address
#     # 4 to  address


def GenerateAnounce(filename):
    columns = [3]
    df = ps.read_excel(filename, usecols=columns)
    # df.loc[4]
    # print(df.item[1])
    # print(df)
    loc = ("announce.xlsx")
    wb = xlrd.open_workbook(loc)

    sheet = wb.sheet_by_index(0)

    print(sheet.row_values(1, 3))
    res = sheet.row_values(1, 3)
    print(type(res[0]))
    if res[0] == "Delhi":
        print("omsa")
    else:
        print("numll")

        # if df.loc[1] == "Bengaluru":
        #     print("osmsa")

        # for index, item in df.iterrows():
        #     # textToSpeech("Sangeetha your" +
        #     #              item['Port'] + "Train has arrived", '1omsai.mp3')
        #     # audios = [f"{i}omsai.mp3" for i in range(1, 12)]

        #     print(df)
        # audioProcessed.export(f"{index}omsai.mp3", format="mp3")

        # if __name__ == "__main__":


GenerateAnounce("announce.xlsx")
song = AudioSegment.from_mp3("1omsai.mp3")
songg = AudioSegment.from_mp3("1_hindi.mp3")
# play(songg)
# play(song)
