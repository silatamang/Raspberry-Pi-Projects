#To display a message on the Sense HAT’s LED matrix
#import library
from sense_hat import SenseHat

# Create a sensehat object
sense = SenseHat()

# Define some colors
blue = (0, 0, 255)
yellow = (255, 255, 0)

#while loop
while True:
    #Display text, set text colour, set background color, scroll speed of the text across LCD screen    
    sense.show_message("Sense HAT is awesome!", text_colour = yellow, back_colour = blue, scroll_speed=0.05)
