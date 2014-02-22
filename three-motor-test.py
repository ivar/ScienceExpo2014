# Jaikrishna
# Initial Date: June 24, 2013
# Last Updated: June 24, 2013
#
# These files have been made available online through a Creative Commons Attribution-ShareAlike 3.0  license.
# (http://creativecommons.org/licenses/by-sa/3.0/)
#
# http://www.dexterindustries.com/
# This code is for testing the BrickPi with a Lego Motor

from BrickPi import *   #import BrickPi.py file to use BrickPi operations

BrickPiSetup()  # setup the serial port for communication

BrickPi.MotorEnable[PORT_A] = 1 #Enable the Motor A
BrickPi.MotorEnable[PORT_B] = 1 #Enable the Motor B
BrickPi.MotorEnable[PORT_C] = 1 #Enable the Motor C

BrickPiSetupSensors()   #Send the properties of sensors to BrickPi



while True:
    print "Motor 3 - Running Forward"
    BrickPi.MotorSpeed[PORT_C] = 100  #Set the speed of MotorA (-255 to 255)
    ot = time.time()
    while(time.time() - ot < 3):    #running while loop for 3 seconds
        BrickPiUpdateValues()       # Ask BrickPi to update values for sensors/motors
        time.sleep(.1)              # sleep for 100 ms
    BrickPiUpdateValues()       # Ask BrickPi to update values for sensors/motors
    time.sleep(1)
    BrickPi.MotorSpeed[PORT_C] = 0  #Set the speed of MotorA (-255 to 255)
    BrickPiUpdateValues()       # Ask BrickPi to update values for sensors/motors
    time.sleep(1)

    print "Motor 1 - Running Forward"
    BrickPi.MotorSpeed[PORT_A] = 200  #Set the speed of MotorA (-255 to 255)
    ot = time.time()
    while(time.time() - ot < 3):    #running while loop for 3 seconds
        BrickPiUpdateValues()       # Ask BrickPi to update values for sensors/motors
        time.sleep(.1)              # sleep for 100 ms
    BrickPiUpdateValues()       # Ask BrickPi to update values for sensors/motors

    print "Motor 2 - Running Forward"
    BrickPi.MotorSpeed[PORT_B] = 200  #Set the speed of MotorA (-255 to 255)
    ot = time.time()
    while(time.time() - ot < 3):    #running while loop for 3 seconds
        BrickPiUpdateValues()       # Bsk BrickPi to update values for sensors/motors
        time.sleep(.1)              # sleep for 100 ms
    BrickPi.MotorSpeed[PORT_B] = 0
    BrickPi.MotorSpeed[PORT_A] = 0
    BrickPiUpdateValues()       # Ask BrickPi to update values for sensors/motors

    BrickPi.MotorSpeed[PORT_A] = -200  #Set the speed of MotorA (-255 to 255)
    ot = time.time()
    while(time.time() - ot < 3):    #running while loop for 3 seconds
        BrickPiUpdateValues()       # Ask BrickPi to update values for sensors/motors
        time.sleep(.1)              # sleep for 100 ms
    BrickPi.MotorSpeed[PORT_A] = 0
    BrickPiUpdateValues()       # Ask BrickPi to update values for sensors/motors

    BrickPi.MotorSpeed[PORT_B] = -200  #Set the speed of MotorA (-255 to 255)
    ot = time.time()
    while(time.time() - ot < 3):    #running while loop for 3 seconds
        BrickPiUpdateValues()       # Bsk BrickPi to update values for sensors/motors
        time.sleep(.1)              # sleep for 100 ms
    BrickPi.MotorSpeed[PORT_B] = 0
    BrickPiUpdateValues()       # Ask BrickPi to update values for sensors/motors

