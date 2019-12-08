'''
Name : Muhamad Arif Lutfi bin Aziz
Date : 7th December 2019

This python script is used as an import function in another file for Arduino-Pi series using Nanpy
Currently it is succesful but only coded just for my FYP (10th November 2019).

Model used : Arduino Uno and Raspberry Pi 3
Raspberry Pi 3 uses Raspbian Stretch as the OS
'''

from nanpy import (ArduinoApi, SerialManager)
from time import sleep

'''
Throw a try and exception to see if the serial communication is established.
User can specify which Arduino connection are they using it on SerialManager()
if they have more than 1 Arduino connected to Raspberry Pi
'''
try:
    connection = SerialManager()
    a = ArduinoApi(connection = connection)
    print("\n==========# Status Report #===========\n")
    print("PASSED_1 : Pi-Arduino communication established.")
    print("\n==========# Status Report #===========\n")
except:
    print("\n==========# Status Report #===========\n")
    print("ERROR 1 - Failure to connect to Arduino UNO.")
    print("\n==========# Status Report #===========\n")

'''
Setup the pin location since Arduino doesn't really understand unless we specify them

Name of the component =  Number/position of pin
'''

E1 = 5 #4
M1 = 4 #For the wheel  #5
E2 = 6 #7
M2 = 7 #For the wheel #6
LED = 13
##0  black, 1 white

sensorR = 14
sensorL = 15

a.pinMode(M1, a.OUTPUT)
a.pinMode(M2, a.OUTPUT)
a.pinMode(LED, a.OUTPUT)
a.pinMode(E1, a.OUTPUT)
a.pinMode(E2, a.OUTPUT)
a.pinMode(sensorR, a.INPUT)
a.pinMode(sensorL, a.INPUT)


## This part of the function is for wheel movementq
def Movements (score, classes, distance, permaStop):
    try:
        while True:
            if (score >= 0.50 and classes == 75 and distance <= 15):
                print("\nMAMAMAMAMA detected, stop!\n")
                permaStop = Terminate(permaStop)
                permaStop = 100
                print("\nBUTTON START 2 = ",permaStop)
                return  permaStop
                break
            elif (score >= 0.50 and classes == 76 and distance <= 15):
                print("\nMMAMAMAMAle detected, stop!\n")
                permaStop = Terminate(permaStop)
                permaStop = 100
                print("\nBUTTON START 2 = ",permaStop)
                return  permaStop
                break
            elif (score >= 0.50 and classes == 77 and distance <= 15):
                print("\nMAMAMAMAAM detected, stop!\n")
                permaStop = Terminate(permaStop)
                print("\nBUTTON START 2 = ",permaStop)
                return  permaStop
                break
            elif (score >= 0.50 and classes == 77 and distance < 35):
                print("\nObstacle detected, stop!\n")
                permaStop = Terminate(permaStop)
                break
            elif (score >= 0.50 and classes == 75 and distance < 35):
                print("\nObstacle detected, stop!\n")
                permaStop = Terminate(permaStop)
                break
            elif (score >= 0.50 and classes == 76 and distance < 35):
                print("\nObstacle detected, stop!\n")
                permaStop = Terminate(permaStop)
                break
            else:
                print("\nNo obstacle is detected : Continue\n")
                Start()
                break
    except:
        a.digitalWrite(M1, a.LOW)
        a.digitalWrite(M2, a.LOW)
        #print("\nWaiting for start instruction.\n")

## This part of the function is for LED blink
## Currently optional (or for testing)
def Blink (score, classes, distance):
    try:
        while True:
            if (score >= 0.50 and classes == 77 and distance < 45):
                print("\nObstacle detected, stop!\n")

                a.digitalWrite(LED, a.LOW)  # High = on, LOW = off
                sleep(0.05) #in Arduino IDE, this is equivalent to 'delay'
                a.digitalWrite(LED,a.HIGH)
                sleep(0.05)
                a.digitalWrite(LED, a.LOW)  # High = on, LOW = off
                sleep(0.05) #in Arduino IDE, this is equivalent to 'delay'
                a.digitalWrite(LED,a.HIGH)
                sleep(0.05)
                break
            elif (score >= 0.50 and classes == 75 and distance < 45):
                print("\nObstacle detected, stop!\n")

                a.digitalWrite(LED, a.LOW)  # High = on, LOW = off
                sleep(0.05) #in Arduino IDE, this is equivalent to 'delay'
                a.digitalWrite(LED,a.HIGH)
                sleep(0.05)
                a.digitalWrite(LED, a.LOW)  # High = on, LOW = off
                sleep(0.05) #in Arduino IDE, this is equivalent to 'delay'
                a.digitalWrite(LED,a.HIGH)
                sleep(0.05)
                break
            elif (score >= 0.50 and classes == 76 and distance < 45):
                print("\nObstacle detected, stop!\n")

                a.digitalWrite(LED, a.LOW)  # High = on, LOW = off
                sleep(0.05) #in Arduino IDE, this is equivalent to 'delay'
                a.digitalWrite(LED,a.HIGH)
                sleep(0.05)
                a.digitalWrite(LED, a.LOW)  # High = on, LOW = off
                sleep(0.05) #in Arduino IDE, this is equivalent to 'delay'
                a.digitalWrite(LED,a.HIGH)
                sleep(0.05)
                break

            else:
                print("\nNo obstacle is detected : Continue\n")
                a.digitalWrite(LED, a.LOW)  # High = gerak, LOW = stop                
                break
    except:
        a.digitalWrite(LED, a.LOW)
        print("\nWaiting for start instruction...\n")
        
def Terminate (permaStop):
    a.digitalWrite(M1, a.LOW)
    a.digitalWrite(M2, a.LOW)
    a.analogWrite(E1, 0)
    a.analogWrite(E2,0)
    permaStop = 100
    print("\nBUTTON START 3 = ",permaStop)
    print("\nModel stopped moving.\n")
    return permaStop

def Start ():
    a.digitalWrite(M1, a.HIGH)
    a.digitalWrite(M2, a.HIGH)
    a.analogWrite(E1, 110)
    a.analogWrite(E2,95)
    val_R = a.digitalRead(sensorR)
    val_L = a.digitalRead(sensorL)
    print("\nModel start moving.\n")
    PathCorrector(val_R, val_L)
    
def PathCorrector(val_R, val_L):

    if(val_R == 0 and val_L == 1): ##if statement for turn left
        a.digitalWrite(M2, a.HIGH)
        a.analogWrite(E2, 200)
        #sleep(0.5)
        #break
    elif(val_R == 1 and val_L == 0): ##if statement for turn right
        a.digitalWrite(M1, a.HIGH)
        a.analogWrite(E1, 190)
        #sleep(0.5)
        #break
    else:
        a.digitalWrite(M2, a.HIGH)
        a.analogWrite(E2, 170)
        a.digitalWrite(M1, a.HIGH)
        a.analogWrite(E1, 170)
    
