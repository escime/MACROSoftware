import time #import the time library for the sleep function
import brickpi3 #import the brickpi3 library
import grovepi #import the grovepi drivers
import conversionLibrary as cl

BP = brickpi3.BrickPi3() #Create an instance of the brickpi to be controlled

time_start = time.time()
ultrasonic_sensor_port = 4
speed = 20 #in cm/s
speedCon = cl.convertSpeed(speed)
turnCt = 0

BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_COLOR_COLOR)

color = ["none", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]

BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A))
BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B))
BP.offset_motor_encoder(BP.PORT_C, BP.get_motor_encoder(BP.PORT_C))
BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))

numberTry = 0

try:
    while grovepi.ultrasonicRead(ultrasonic_sensor_port) > 15:
        try:
            value = BP.get_sensor(BP.PORT_1)
            turnCt = turnCt + 1
            if(color[value] == "Blue"):
                BP.set_motor_power(BP.PORT_A+BP.PORT_D, speedCon*0.5)
                value = BP.get_sensor(BP.PORT_1)
            if(color[value] != "Blue" and (turnCt%2) == 0):
                time_start = time.time()
                if(numberTry == 3):
                    break
                while color[value] != "Blue":
                    BP.set_motor_power(BP.PORT_A, speedCon*0.6)
                    BP.set_motor_power(BP.PORT_D, speedCon*0.2)
                    value = BP.get_sensor(BP.PORT_1)
                    if(time.time() - time_start > 1 and numberTry < 2):
                        numberTry = numberTry + 1
                        break
            else:
                time_start = time.time()
                if(numberTry == 3):
                    break
                while color[value] != "Blue":
                    BP.set_motor_power(BP.PORT_D, speedCon*0.6)
                    BP.set_motor_power(BP.PORT_A, speedCon*0.2)
                    value = BP.get_sensor(BP.PORT_1)
                    if(time.time() - time_start > 1 and numberTry < 2):
                        numberTry = numberTry + 1
                        break
        except brickpi3.SensorError as error:
            print(error)
        
        time.sleep(0.02)
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