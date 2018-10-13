import time #import the time library for the sleep function
import brickpi3 #import the brickpi3 library
import grovepi #import the grovepi drivers

BP = brickpi3.BrickPi3() #Create an instance of the brickpi to be controlled

ultrasonic_sensor_port = 4

try:
    while grovepi.ultrasonicRead(ultrasonic_sensor_port) > 5:
        print(grovepi.acc_xyz())
except IOError as error:
	print(error)
except TypeError as error:
	print(error)
except KeyboardInterrupt:
	print("You pressed ctrl+C...")
    
BP.reset_all()