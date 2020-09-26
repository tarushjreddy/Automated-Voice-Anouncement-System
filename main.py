from gtts import gTTS
from pydub import AudioSegment
import pandas as ps
import os
from playsound import playsound
from pydub.playback import play
import xlrd
from datetime import datetime
df = ps.read_excel("announce.xlsx")
print(df)

now = datetime.now()

print(now.strftime("%d/%m/%Y %H:%M:%S"))
print(type(now.strftime("%H")))
print(type(int(now.strftime("%H"))))


def textToSpeech(text, filename):
    mytext = str(text)
    language = 'en'
    myobj = gTTS(slow=False, lang=language, text=mytext)
    myobj.save(filename)


def Evaluvation(filename):
    wb = xlrd.open_workbook(filename)

    sheet = wb.sheet_by_index(0)

    des = sheet.row_values(1, 4)
    print(des[0])
    tabb = []
    minn = []
    kkk = []
    train = []
    dest = []
    plat = []

  #  details = now.strftime("%d : :%H : %M")

    for i in range(4):
        tab = sheet.row_values(i + 1, 4)
        tabone = sheet.row_values(i + 1, 5)
        tabtwo = sheet.row_values(i + 1, 7)
        kkk.append(tabtwo[0])
        tabthree = sheet.row_values(i + 1, 2)

        train.append(tabthree[0])

        minn.append(tabone[0])
        tabb.append(tab[0])
        dest.append(tabthree[1])
        plat.append(tabthree[7])

        if int(tabb[i]) == int(now.strftime("%H")) and int(minn[i]) == int(now.strftime("%M")) and int(kkk[i]) == int(
                now.strftime("%d")):

            textToSpeech(dest[i] + "Train Heading towards" + train[i] + "  " +
                         " has arrived" + "at Platform number" + str(plat[i]) + "", '1omsai.mp3')
            textToSpeech("Passengers are requested to board the train from" +
                         "at Platform number" + str(plat[i]), 'later.mp3')

            alert = AudioSegment.from_mp3("Voice 002-mc..mp3")
            play(alert)
            song = AudioSegment.from_mp3("1omsai.mp3")

            play(song)
            play(alert)
            songone = AudioSegment.from_mp3("later.mp3")
            play(songone)

            play(alert)

            print(f"{tabb[i]} is omsairam")
            break
        else:
            print("hello")
            break

    print(minn)


Evaluvation("announce.xlsx")
