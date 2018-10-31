import brickpi3
import time

BP = brickpi3.BrickPi3()

def raiseLift():
    try:
        BP.offset_motor_encoder(BP.PORT_C, BP.get_motor_encoder(BP.PORT_C))
        while(BP.get_motor_encoder(BP.PORT_C) < 360):
            BP.set_motor_power(BP.PORT_C+BP.PORT_B, 50)
        BP.set_motor_power(BP.PORT_C+BP.PORT_B, 0)
    except IOError as error:
        print(error)
    except TypeError as error:
        print(error)
    except KeyboardInterrupt:
        print("You pressed ctrl+C...")
        BP.reset_all()

def maintainLift(time_len):
    try:
        current = BP.get_motor_encoder(BP.PORT_C)
        time_start = time.time()
        while(time.time() - time_start < time_len):
            if(BP.get_motor_encoder(BP.PORT_C) < current-3):
                while(BP.get_motor_encoder(BP.PORT_C) < current+3):
                    BP.set_motor_power(BP.PORT_C+BP.PORT_B, 50)
            else:
                BP.set_motor_power(BP.PORT_C+BP.PORT_B, 0)
            time.sleep(0.02)
    except IOError as error:
        print(error)
    except TypeError as error:
        print(error)
    except KeyboardInterrupt:
        print("You pressed ctrl+C...")
        BP.reset_all()

def getLiftPosition():
    try:
        return BP.get_motor_encoder(BP.PORT_C)
    except IOError as error:
        print(error)
    except TypeError as error:
        print(error)
    except KeyboardInterrupt:
        print("You pressed ctrl+C...")

def maintainLiftInc(current):
    try:
        if(BP.get_motor_encoder(BP.PORT_C) < current-3):
            BP.set_motor_power(BP.PORT_C+BP.PORT_B,50)
        else:
            BP.set_motor_power(BP.PORT_C+BP.PORT_B,0)
    except IOError as error:
        print(error)
    except TypeError as error:
        print(error)
    except KeyboardInterrupt:
        print("You pressed ctrl+C...")
        BP.reset_all()

def lowerLift():
    try:
        BP.offset_motor_encoder(BP.PORT_C, BP.get_motor_encoder(BP.PORT_C))
        while(BP.get_motor_encoder(BP.PORT_C) > -360):
            BP.set_motor_power(BP.PORT_C+BP.PORT_B, -50)
        BP.set_motor_power(BP.PORT_C+BP.PORT_B, 0)
    except IOError as error:
        print(error)
    except TypeError as error:
        print(error)
    except KeyboardInterrupt:
        print("You pressed ctrl+C...")
        BP.reset_all()