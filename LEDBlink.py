from nanpy import (ArduinoApi, SerialManager)
from time import sleep

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

LED = 13

a.pinMode(LED,a.OUTPUT)

def BlinkLED():
	try:
		while True:
			a.digitalWrite(LED, a.HIGH)
			sleep(1)
			a.digitalWrite(LED, a.LOW)
			sleep(1)
	except:
		print("Error! LED is turned off.")
		a.digitalWrite(LED, a.LOW)
