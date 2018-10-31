import brickpi3 #import the brickpi3 library
import conversionLibrary as cl
import time

BP = brickpi3.BrickPi3() #Create an instance of the brickpi to be controlled

BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_GYRO_ABS_DPS)

def straightDrive(distance, speed):
    distanceEncoder = cl.convertEncoder(distance)
    print(distanceEncoder)
    speedCon = cl.convertSpeed(speed)

    BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A))
    BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B))
    BP.offset_motor_encoder(BP.PORT_C, BP.get_motor_encoder(BP.PORT_C))
    BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))

    try:
        if(distanceEncoder > 0):
            while BP.get_motor_encoder(BP.PORT_A) < distanceEncoder:
                try:
                    heading = BP.get_sensor(BP.PORT_3)[0]
                except brickpi3.SensorError as error:
                    print(error)
                BP.set_motor_power(BP.PORT_A+BP.PORT_D, speedCon)
                if(heading >= 2):
                    while heading >= 1:
                        try:
                            heading = BP.get_sensor(BP.PORT_3)[0]
                        except brickpi3.SensorError as error:
                            print(error)
                        BP.set_motor_power(BP.PORT_A, speedCon*0.7)
                        BP.set_motor_power(BP.PORT_D, speedCon)
                if(heading <= -2):
                    while heading <= -1:
                        try:
                            heading = BP.get_sensor(BP.PORT_3)[0]
                        except brickpi3.SensorError as error:
                            print(error)
                        BP.set_motor_power(BP.PORT_D, speedCon*0.7)
                        BP.set_motor_power(BP.PORT_A, speedCon)
        if(distanceEncoder < 0):
            speedCon = -1 * speedCon
            while BP.get_motor_encoder(BP.PORT_A) > distanceEncoder:
                try:
                    heading = BP.get_sensor(BP.PORT_3)[0]
                except brickpi3.SensorError as error:
                    print(error)
                BP.set_motor_power(BP.PORT_A+BP.PORT_D, speedCon)
                if(heading >= 2):
                    while heading >= 1:
                        try:
                            heading = BP.get_sensor(BP.PORT_3)[0]
                        except brickpi3.SensorError as error:
                            print(error)
                        BP.set_motor_power(BP.PORT_A, speedCon*0.7)
                        BP.set_motor_power(BP.PORT_D, speedCon)
                if(heading <= -2):
                    while heading <= -1:
                        try:
                            heading = BP.get_sensor(BP.PORT_3)[0]
                        except brickpi3.SensorError as error:
                            print(error)
                        BP.set_motor_power(BP.PORT_D, speedCon*0.7)
                        BP.set_motor_power(BP.PORT_A, speedCon)

    except IOError as error:
        print(error)
    except TypeError as error:
        print(error)
    except KeyboardInterrupt:
        print("You pressed ctrl+C...")
        BP.reset_all()

    BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A))
    BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B))
    BP.offset_motor_encoder(BP.PORT_C, BP.get_motor_encoder(BP.PORT_C))
    BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))

    BP.reset_all()

def rotateDrive(setHeading):
    try:
        try:
            heading = BP.get_sensor(BP.PORT_3)[0]
        except brickpi3.SensorError as error:
            print(error)
        if(setHeading > heading):
            while(heading < setHeading):
                BP.set_motor_power(BP.PORT_A,70)
                BP.set_motor_power(BP.PORT_D,-70)
                try:
                    heading = BP.get_sensor(BP.PORT_3)[0]
                    print(heading)
                except brickpi3.SensorError as error:
                    print(error)
                time.sleep(0.02)
        if(setHeading < heading):
            while(heading > setHeading):
                BP.set_motor_power(BP.PORT_A,-70)
                BP.set_motor_power(BP.PORT_D,70)
                try:
                    heading = BP.get_sensor(BP.PORT_3)[0]
                    print(heading)
                except brickpi3.SensorError as error:
                    print(error)
                time.sleep(0.02)
    except IOError as error:
        print(error)
    except TypeError as error:
        print(error)
    except KeyboardInterrupt:
        print("You pressed ctrl+C...")
        BP.reset_all()
    BP.reset_all()