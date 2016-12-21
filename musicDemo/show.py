import leda
import time
import json
import vlc
from leda import color

leda.ser = leda.serial.Serial('COM6',250000)
time.sleep(2)

l = leda.led()
l.setLength(180)

f = open('music.json','r')
music = f.read()
f.close()

m = json.loads(music)

it = [0,0,0,0,0,0,0,0]
a = [0,0,0,0,0,0,0,0]
p = vlc.MediaPlayer("file:///Samurai.mp3")
p.play()
time.sleep(0.2)
bt = time.time()
e = True

while e:
    for i in range(180):
        l.setPixel(i,color())

    ct = time.time()
    for i in range(8):
        if it[i]<len(m[i]):
            if m[i][it[i]][0]<ct-bt: it[i]+=1


    for i in range(8):
        a[i] = 0
        if it[i]!=0:
            if m[i][it[i]-1][1]+m[i][it[i]-1][0]>ct-bt:
                if m[i][it[i]-1][1]+m[i][it[i]-1][0]-ct+bt<=0.3:
                    a[i]=(m[i][it[i]-1][1]+m[i][it[i]-1][0]-ct+bt)*3.333
                else:
                    a[i]=1
        if it[i]<len(m[i]):
            if m[i][it[i]][0]>ct-bt:
                if m[i][it[i]][0]-ct+bt<=0.3:
                    a[i]=(m[i][it[i]][0]-ct+bt)*3.333

    for i in range(180):
        l.setPixel(i,color(30,30,30,a[0]))

    for i in range(180):
        if int(i/6)%3 == 0: l.setPixel(i,color(0,255,255,a[1]))

    for i in range(180):
        if int(i/6)%3 == 1: l.setPixel(i,color(100,255,0,a[2]))

    for i in range(180):
        if int(i/6)%3 == 2: l.setPixel(i,color(255,0,100,a[3]))

    for i in range(180):
        if int(i/6)%3 == 2: l.setPixel(i,color(255,0,40,a[4]))

    for i in range(180):
        if int(i/3)%6 == 0: l.setPixel(i,color(255,90,0,a[5]))

    for i in range(180):
        if int(i/3)%6 == 2: l.setPixel(i,color(230,0,255,a[6]))

    for i in range(180):
        if int(i/3)%6 == 4: l.setPixel(i,color(40,0,255,a[7]))
    l.send()
    e = False
    for i in range(8):
        if it[i]<len(m[i]):
            e = True
