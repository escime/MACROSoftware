import time
import brickpi3

BP = brickpi3.BrickPi3()

BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_COLOR_REFLECTED)

def printReadings():
    try:
        while True:
            currentValue = BP.get_sensor(BP.PORT_1)
            print("Current reading: ", currentValue)
            time.sleep(0.02)
    except brickpi3.SensorError as error:
        print(error)
    except KeyboardInterrupt:
        BP.reset_all()