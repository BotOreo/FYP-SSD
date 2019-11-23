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

value = 0
LED = 13

a.pinMode(LED,a.OUTPUT)

try:
    while True:
        if value <= 3 :
            a.digitalWrite(LED, a.HIGH)
            sleep(0.8)
            a.digitalWrite(LED, a.LOW)
            sleep(0.8)
            value=value+0.1
        else :
            break
        
        

except:
    print("Error! LED is turned off.")
    a.digitalWrite(LED, a.LOW)
