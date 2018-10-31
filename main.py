# MACRO Software
# File: main.py
# Date: 10 October 2018
# By: Ethan Edward Scime
# escime
# By: David Craig Hayward
# dhaywar
# Meghana Neena Jayaraman
# jayaramm
# Elizabeth Marie McCleery
# emccleer
# Section: 2
# Team: 33
#
# ELECTRONIC SIGNATURE
# Ethan Edward Scime
# David Craig Howard
# Meghana Neena Jayaraman
# Elizabeth Marie McCleery
#
# The electronic signatures above indicate that the program
# submitted for evaluation is the combined effort of all
# team members and that each member of the team was an
# equal participant in its creation. In addition, each
# member of the team has a general understanding of
# all aspects of the program development and execution.
#
# The main software running onboard the raspberry PI.
import time
import driveStraightDist as dsd
import AmbientReading as ar
import GuidelineTracking as gt
import LiftControls as lc
import DriveHeading as dh
import DriveStraightLiftMaintain as dslm

print("Avalible functions: ")
print("1. Drive at Selected Speed and Distance")
print("2. Output Ambient Light Sensor Readings")
print("3. Follow Line")
print("4. Lift Control Testing")
print("5. Test Heading Drive")
print("6. Test Heading Rotation")
print("7. Drive with maintainLift")
userSelect = int(input("What function would you like to select? "))

if(userSelect == 1):
    distance = float(input("What distance would you like the robot to travel (cm)? "))
    speed = float(input("What speed would you like the robot to travel at (cm/s)? "))
    dsd.straightDrive(distance, speed)

if(userSelect == 2):
    ar.printReadings()

if(userSelect == 3):
    maxSpeed = float(input("What would you like the maximum speed to be? "))
    gt.guidelineFollow(maxSpeed)
    
if(userSelect == 4):
    lc.raiseLift()
    lc.maintainLift(1)
    lc.lowerLift()
    
if(userSelect == 5):
    distance = float(input("What distance would you like the robot to travel (cm)? "))
    speed = float(input("What speed would you like the robot to travel at (cm/s)? "))
    dh.straightDrive(distance, speed)
    
if(userSelect == 6):
    heading = int(input("What heading would you like to turn to (degrees)? "))
    dh.rotateDrive(heading)
    
if(userSelect == 7):
    distance = float(input("What distance would you like the robot to travel (cm)? "))
    speed = float(input("What speed would you like the robot to travel at (cm/s)? "))
    lc.raiseLift()
    time.sleep(3)
    dslm.straightDrive(distance, speed)
    lc.lowerLift()