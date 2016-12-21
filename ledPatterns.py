import led
import time
from led import color
import random
import threading

a = led.led()

style = 'rainbow'

def loop():
    t2 = 0
    while True:
        if style == 'blank':
            for i in range(180):
                a.setPixel(i,color())
        if style == 'rainbow':
            t = time.time() * 20
            for i in range(180):
                a.setPixel(i,led.hslToRgb(round((i+t)*4)%360,100,20))
        if style == 'rainbow2':
            t = time.time() * 30
            for i in range(180):
                a.setPixel(i,led.hslToRgb(round((i+t)*16)%360,100,20))
        if style == 'normal':
            t = int(round(time.time() * 4))
            for i in range(180):
                if (i+t)%3 == 0:
                    a.setPixel(i,color(60,0,0))
                if (i+t)%3 == 1:
                    a.setPixel(i,color(60, 55, 0))
                if (i+t)%3 == 2:
                    a.setPixel(i,color(0,60,0))
        if style == 'normal2':
            t = int(round(time.time() * 4))
            for i in range(180):
                if (i+t)%3 == 0:
                    a.setPixel(i,color(128,255,0))
                if (i+t)%3 == 1:
                    a.setPixel(i,color(255,0,255))
                if (i+t)%3 == 2:
                    a.setPixel(i,color(0,255,255))
        if style == 'cancer':
            for i in range(180):
                if (i+t2)%2 == 0:
                    a.setPixel(i,color(255,0,0))
                else:
                    a.setPixel(i,color(0,255,255))
            t2+=1
        if style == 'cancer2':
            t = int(round(time.time() * 2))
            for i in range(180):
                if t%2 == 0:
                    if (i+t2)%2 == 0:
                        a.setPixel(i,color(255,0,0))
                    else:
                        a.setPixel(i,color(0,255,255))
                else:
                    if (i+t2)%2 == 0:
                        a.setPixel(i,color(0,0,255))
                    else:
                        a.setPixel(i,color(255,255,0))
            t2+=1
        if style == 'random':
            for k in range(20):
                a.setPixel(random.randint(0,179),color(random.randint(0,128),random.randint(0,80),random.randint(0,80)))
        a.send()
        time.sleep(0.0001)

def init():
    a.setLength(180)
    t = threading.Thread(target=loop)
    t.daemon = True
    t.start()
