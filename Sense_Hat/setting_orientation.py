from sense_hat import SenseHat
from time import sleep

#To display a message on the Sense HAT’s LED matrix
sense = SenseHat()

# Define some colors
w = (150, 150, 150)
b = (0, 0, 255)
e = (0, 0, 0)

#Define where each color will be displayed on sense HAT’s LED matrix
image = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
w,w,w,e,e,w,w,w,
w,w,b,e,e,w,w,b,
w,w,w,e,e,w,w,w,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

sense.set_pixels(image)

#while loop
while True:
    sleep(1)		#pause Python program for 1 second
    sense.flip_h()		#flip the LED horizontally
