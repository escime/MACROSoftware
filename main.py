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
import driveStraightDist as dsd

distance = float(input("What distance would you like the robot to travel (cm)? "))
speed = float(input("What speed would you like the robot to travel at (cm/s)? "))

dsd.straightDrive(distance, speed)