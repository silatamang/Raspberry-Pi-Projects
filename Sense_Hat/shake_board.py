from sense_hat import SenseHat

# Create a sensehat object
sense = SenseHat()

red = (255, 0, 0)

while True:
	acceleration = sense.get_accelerometer_raw
	x = acceleration['x']
	y = acceleration['y']
    z = acceleration['z']

# abs() function gives us the absolute figure of a value and ignores whether the actual value is positive or negative 
x = abs(x)
y = abs(y)
z = abs(z)

if x >1 or y > 1 or z >1:
	sense.show_letter("!", red)
else:
    sense.clear()
