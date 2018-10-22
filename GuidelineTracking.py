#This class is for all variations of line following code.
import brickpi3
import time
import conversionLibrary as cl

BP = brickpi3.BrickPi3()
def guidelineFollow(maxSpeed):
    speedCon = cl.convertSpeed(maxSpeed)
    speedFind = cl.convertSpeed(-35)
    BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A))
    BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))
    BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_COLOR_REFLECTED)
    try:
        BP.get_sensor(BP.PORT_1)
    except brickpi3.SensorError:
        print("Configuring...")
        error = True
        while error:
            time.sleep(0.1)
            try:
                BP.get_sensor(BP.PORT_1)
                error = False
            except brickpi3.SensorError:
                error = True
    print("Configured.")
    try:
        while(True):
              currentValue = BP.get_sensor(BP.PORT_1)
              if(currentValue < 10):
                  while True:
                      if(currentValue < 10):
                          BP.set_motor_power(BP.PORT_A, speedCon*0.5)
                          BP.set_motor_power(BP.PORT_D, -speedCon)
                      if(currentValue > 10):
                          BP.set_motor_power(BP.PORT_A, -speedCon)
                          BP.set_motor_power(BP.PORT_D, speedCon*0.5)
                      currentValue = BP.get_sensor(BP.PORT_1)
                      time.sleep(0.05)
              if(currentValue >= 10):
                  BP.set_motor_power(BP.PORT_A, speedFind)
                  BP.set_motor_power(BP.PORT_D, speedFind)
                  print("check")
              time.sleep(0.02)
    except IOError as error:
        print(error)
    except TypeError as error:
        print(error)
    except KeyboardInterrupt:
        BP.reset_all()
        print("You pressed ctrl+C...")
    except brickpi3.SensorError as error:
        print(error)