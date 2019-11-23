'''
Name : Muhamad Arif Lutfi bin Aziz
Date : 10th November 2019

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

E1 = 4
M1 = 5 #For the wheel
E2 = 7
M2 = 6 #For the wheel
LED = 13

a.pinMode(M1, a.OUTPUT)
a.pinMode(M2, a.OUTPUT)
a.pinMode(LED, a.OUTPUT)

## This part of the function is for wheel movement
def Movements (score, classes):
    try:
        while True:
            if (score >= 0.50 and classes == 87):
                print("\nObject detected, stop!\n")
                a.digitalWrite(M1, a.LOW) # High = gerak, LOW = stop
                a.digitalWrite(M2, a.LOW)
                break
            else:
                print("\nNo object is detected : Continue\n")
                a.digitalWrite(M1, a.HIGH)  # High = gerak, LOW = stop
                a.digitalWrite(M2, a.HIGH)
                break
    except:
        a.digitalWrite(M1, a.LOW)
        a.digitalWrite(M2, a.LOW)
        print("\nOops. Something went wrong. The robot will be stopped to avoid damages.\n")

## This part of the function is for LED blink
## Currently optional (or for testing)
## We can separate this if-else into 2 parts if we have multiple object type to detect
def Blink (score, classes):
    try:
        while True:
            if (score >= 0.50 and classes == 87): 
		
                print("\nObject detected, stop!\n")

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
                print("\nNo object is detected : Continue\n")
                a.digitalWrite(LED, a.LOW)  # High = gerak, LOW = stop                
                break
    except:
        a.digitalWrite(LED, a.LOW)
        print("\nOops. Something went wrong. LED is turned off to avoid damages.\n")
        
def Terminate ():
    try:
        a.digitalWrite(M1, a.LOW)
        a.digitalWrite(M2, a.LOW)
        print("\nProgram is terminated.\n")
        
            
    except:
        print("\nOops. Something went wrong.\n")



