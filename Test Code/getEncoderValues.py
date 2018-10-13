# wallstop.py
import time #import the time library for the sleep function
import brickpi3 #import the brickpi3 library
import grovepi #import the grovepi drivers

BP = brickpi3.BrickPi3() #Create an instance of the brickpi to be controlled

ultrasonic_sensor_port = 4 #Set which port the ultrasonic sensor is connected to

try:
	while grovepi.ultrasonicRead(ultrasonic_sensor_port) > 15: #Run loop until the ultrasonic sensor reads a value less than or equal to 15
		print("Sensor: %6d Motor A: %6d  B: %6d  C: %6d  D: %6d" \
			% (grovepi.ultrasonicRead(ultrasonic_sensor_port), \
				BP.get_motor_encoder(BP.PORT_A), \
				BP.get_motor_encoder(BP.PORT_B), \
				BP.get_motor_encoder(BP.PORT_C), \
				BP.get_motor_encoder(BP.PORT_D)))
except IOError as error:
	print(error)
except TypeError as error:
	print(error)
except KeyboardInterrupt:
	print("You pressed ctrl+C...")

#Reset all motor enconder values
BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A))
BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B))
BP.offset_motor_encoder(BP.PORT_C, BP.get_motor_encoder(BP.PORT_C))
BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))

BP.reset_all()
