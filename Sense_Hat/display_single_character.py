#import libraries
from sense_hat import SenseHat
from time import sleep
from random import randint

#To display a message on the Sense HAT’s LED matrix
## Create a sensehat object
sense = SenseHat()

# Define some colors
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

white = (255, 255, 255)
yellow = (255, 255, 0)

# Generate a random colour
def pick_random_colour():
     #Generate random integers between 0 and 255 using randint function
     random_red = randint(0, 255)		
     random_green = randint(0, 255)
     random_blue = randint(0, 255)
     return (random_red, random_green, random_blue)

sense.show_letter("L", pick_random_colour())
sleep(1)		#sleep function to temporarily pause your Python program for 1 second
sense.show_letter("a", pick_random_colour())
sleep(1)		#sleep function to temporarily pause your Python program for 1 second
sense.show_letter("u", pick_random_colour())
sleep(1)		#sleep function to temporarily pause your Python program for 1 second
sense.show_letter("r", pick_random_colour())
sleep(1)		#sleep function to temporarily pause your Python program for 1 second
sense.show_letter("a", pick_random_colour())

sleep(1)		#sleep function to temporarily pause your Python program for 1 second

#Clear LED matrix
sense.clear()

