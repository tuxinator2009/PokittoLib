# uPyGame performance test
# 1) Drawing a surface of 16x16 pixels 100 times a frame gives 16 Fps (full speed). 4-bit colors for both screen and the surface.  
# 2) Drawing a surface of 16x16 pixels 200 times a frame gives 12 Fps (full speed). 4-bit colors for both screen and the surface.  

import upygame as upg
import framebuf
import urandom as random

upg.display.init()
screen_sf = upg.display.set_mode() # full screen

# pokitto picture
w2 = 16
h2 = 16
pokittoPixels = [
0x00,0x03,0x33,0x33,0x33,0x33,0x33,0x00,
0x00,0x32,0x22,0x22,0x22,0x22,0x32,0x00,
0x00,0x32,0x33,0x33,0x33,0x33,0x22,0x00,
0x00,0x32,0x31,0x11,0x11,0x11,0x22,0x00,
0x00,0x32,0x31,0x13,0x11,0x31,0x22,0x00,
0x02,0x32,0x31,0x11,0x11,0x11,0x22,0x23,
0x03,0x32,0x31,0x13,0x33,0x11,0x22,0x30,
0x00,0x32,0x31,0x11,0x11,0x11,0x22,0x00,
0x00,0x32,0x22,0x22,0x22,0x22,0x22,0x00,
0x00,0x32,0x23,0x22,0x22,0x23,0x32,0x00,
0x00,0x32,0x33,0x32,0x23,0x33,0x32,0x00,
0x00,0x32,0x23,0x22,0x23,0x32,0x22,0x00,
0x00,0x32,0x22,0x23,0x32,0x22,0x22,0x00,
0x00,0x32,0x22,0x22,0x22,0x22,0x32,0x00,
0x00,0x33,0x33,0x33,0x33,0x33,0x33,0x00,
0x00,0x32,0x00,0x00,0x00,0x00,0x32,0x00,
]
pokittoBuf = bytearray(pokittoPixels)

#test
#pokittoFBuf = framebuf.FrameBuffer(pokittoBuf, w2, h2, framebuf.GS4_HMSB)

hero_sf = upg.surface.Surface(w2, h2, pokittoBuf)
#hero_sf.fill(2)

x=20
y=20
vx = 0;
vy = 0;
while True:

    eventtype = upg.event.poll()
    if eventtype != upg.NOEVENT:
        if eventtype.type() == upg.KEYDOWN:
            if eventtype.key() == upg.K_RIGHT:
                vx = 1
            if eventtype.key() == upg.K_LEFT:
                vx = -1
            if eventtype.key() == upg.K_UP:
                vy = -1
            if eventtype.key() == upg.K_DOWN:
                vy = 1
        if eventtype.type() == upg.KEYUP:
            if eventtype.key() == upg.K_RIGHT:
                vx = 0
            if eventtype.key() == upg.K_LEFT:
                vx = 0
            if eventtype.key() == upg.K_UP:
                vy = 0
            if eventtype.key() == upg.K_DOWN:
                vy = 0

    for i in range(1,200):
        x2 = random.getrandbits(6) + 20
        y2 = random.getrandbits(6) + 5
        screen_sf.blit(hero_sf, x2, y2)

    x = x + vx
    y = y + vy
    screen_sf.blit(hero_sf, x, y)

    upg.display.flip()
