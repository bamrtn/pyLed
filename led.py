import serial
import time

class color:
    r = 0
    g = 0
    b = 0
    def __init__(self, _r=0, _g=0, _b=0):
        self.r = _r
        self.g = _g
        self.b = _b

def hslToRgb(h, s, l):
    h = h/360
    s = s/100
    l = l/100
    o = color()
    if (s == 0):
        o.r = o.g = o.b = math.floor(l)
    else:
        def hue(p, q, t):
            if t < 0: t += 1
            if t > 1: t -= 1
            if t < 1/6: return p + (q - p) * 6 * t
            if t < 1/2: return q
            if t < 2/3: return p + (q - p) * (2/3 - t) * 6
            return p

        q = l * (1 + s) if l < 0.5 else l + s - l * s
        p = 2 * l - q
        o.r = round(hue(p, q, h + 1/3) * 255)
        o.g = round(hue(p, q, h) * 255)
        o.b = round(hue(p, q, h - 1/3) * 255)

    return o

class led:
    pixels = []
    f = 0
    def send(self):
        message = bytes([])
        for i in self.pixels:
            message += bytes([i.r,i.g,i.b])
        ser.write(message)
        if self.f == 0:
            self.f = 1
        while ser.read() != bytes('k','ascii'):
            time.sleep(0.001)
    def setLength(self, len):
        self.pixels = [color()] * len
    def setPixel(self, pos, c):
        self.pixels[pos] = c
