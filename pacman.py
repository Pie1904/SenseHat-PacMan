from sense_hat import SenseHat
import time

sense = SenseHat()

y = [255,255,0]
e = [0,0,0]
t = [255,0,0]
g = [0,255,0]


image = [
        e,e,e,y,y,y,e,e,
        e,e,y,y,y,y,y,e,
        e,y,y,y,y,e,e,g,
        e,y,y,y,e,e,t,t,
        e,y,y,y,e,e,t,t,
        e,y,y,y,y,e,e,e,
        e,e,y,y,y,y,y,e,
        e,e,e,y,y,y,e,e,
        ]
   


image2 = [
    e,e,e,y,y,y,e,e,
    e,e,y,y,y,y,y,e,
    e,y,y,y,y,y,g,y,
    e,y,y,y,y,t,t,e,
    e,y,y,y,y,t,t,e,
    e,y,y,y,y,y,y,y,
    e,e,y,y,y,y,y,e,
    e,e,e,y,y,y,e,e,
        ]

image3 = [
    e,e,e,y,y,y,e,e,
    e,e,y,y,y,y,y,e,
    e,y,y,y,y,y,y,y,
    e,y,y,y,y,y,y,y,
    e,y,y,y,y,y,y,y,
    e,y,y,y,y,y,y,y,
    e,e,y,y,y,y,y,e,
    e,e,e,y,y,y,e,e,
        ]


image4 = [
    e,e,e,y,y,y,e,e,
    e,e,y,y,y,y,y,e,
    e,y,y,y,y,y,y,e,
    e,y,y,y,y,y,e,t,
    e,y,y,y,y,y,e,t,
    e,y,y,y,y,y,y,e,
    e,e,y,y,y,y,y,e,
    e,e,e,y,y,y,e,e,
        ]


while True:
    sense.set_pixels(image)
    time.sleep(0.45)
    sense.set_pixels(image2)
    time.sleep(0.45)
    sense.set_pixels(image3)
    time.sleep(0.45)
    sense.set_pixels(image4)
    time.sleep(0.25)

