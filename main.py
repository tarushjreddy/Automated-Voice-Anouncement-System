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
    # loc = ("announce.xlsx")
    wb = xlrd.open_workbook(filename)

    sheet = wb.sheet_by_index(0)
    # print(sheet.row_values(1, 3))
    des = sheet.row_values(1, 4)
    print(des[0])
    tabb = []
    minn = []
    kkk = []
    details = now.strftime("%d : :%H : %M")
    for i in range(4):
        tab = sheet.row_values(i+1, 4)
        tabone = sheet.row_values(i+1, 5)
        tabtwo = sheet.row_values(i+1, 7)
        kkk.append(tabtwo[0])

        # print(tab)
        minn.append(tabone[0])
        tabb.append(tab[0])
        # print(int(tabb[1]))
    # date = int(tabb)
        # print(tabone[0])
        textToSpeech("Sangeetha your" +
                     "Train has arrived", '1omsai.mp3')
        if int(tabb[i]) == int(now.strftime("%H")) and int(minn[i]) == int(now.strftime("%M")) and int(kkk[i]) == int(now.strftime("%d")):
            textToSpeech("Sangeetha your" +
                         "Train has arrived", '1omsai.mp3')
            print(f"{tabb[i]} is omsairam")
        else:
            print(
                f"{kkk[i]} Day {tabb[i]} Hours {minn[i]} Minutes  \tnot defined")

    print(minn)


Evaluvation("announce.xlsx")
