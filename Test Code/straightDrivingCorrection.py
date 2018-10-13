import time #import the time library for the sleep function
import brickpi3 #import the brickpi3 library
import grovepi #import the grovepi drivers
import conversionLibrary as cl

BP = brickpi3.BrickPi3() #Create an instance of the brickpi to be controlled

distance = 200 #in cm
distanceEncoder = cl.convertEncoder(distance)
speed = 25 #in cm/s
speedCon = cl.convertSpeed(speed)

BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A))
BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B))
BP.offset_motor_encoder(BP.PORT_C, BP.get_motor_encoder(BP.PORT_C))
BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))

try:
    while BP.get_motor_encoder(BP.PORT_A) < distanceEncoder:
        differential = BP.get_motor_encoder(BP.PORT_A) - BP.get_motor_encoder(BP.PORT_D)
        BP.set_motor_power(BP.PORT_A+BP.PORT_B, speedCon)
        if(differential >= 3):
            while differential >= 1:
                differential = BP.get_motor_encoder(BP.PORT_A) - BP.get_motor_encoder(BP.PORT_D)
                BP.set_motor_power(BP.PORT_A, speedCon*0.7)
                BP.set_motor_power(BP.PORT_D, speedCon)
        if(differential <= -3):
            while differential <= -1:
                differential = BP.get_motor_encoder(BP.PORT_A) - BP.get_motor_encoder(BP.PORT_D)
                BP.set_motor_power(BP.PORT_D, speedCon*0.7)
                BP.set_motor_power(BP.PORT_A, speedCon)
except IOError as error:
	print(error)
except TypeError as error:
	print(error)
except KeyboardInterrupt:
	print("You pressed ctrl+C...")

BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A))
BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B))
BP.offset_motor_encoder(BP.PORT_C, BP.get_motor_encoder(BP.PORT_C))
BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))

BP.reset_all()