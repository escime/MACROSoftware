def convertSpeed(speedInput):
    outputVoltage = (speedInput/43.3) * 100
    return outputVoltage

def convertDistance(centi):
    outputMilli = centi/10
    return outputMilli

def convertEncoder(centi):
    encoderCt = centi*20.9
    return encoderCt
