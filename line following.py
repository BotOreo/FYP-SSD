E1 = 5 #4
M1 = 4 #For the wheel  #5
E2 = 6 #7
M2 = 7 #For the wheel #6
LED = 13

a.pinMode(M1, a.OUTPUT)
a.pinMode(M2, a.OUTPUT)
a.pinMode(E1, a.OUTPUT)
a.pinMode(E2, a.OUTPUT)

def forward(valueR,valueL):
    a.digitalWrite(M1, a.HIGH)
    a.digitalWrite(M2, a.HIGH)
    a.analogWrite(E1, a.valueR)
    a.analogWrite(E2, a.valueL)

def backward(valueR,valueL):
    a.digitalWrite(M1, a.LOW)
    a.digitalWrite(M2, a.LOW)
    a.analogWrite(E1, a.valueR)
    a.analogWrite(E2, a.valueL)

def stop(valueR,valueL):
    a.digitalWrite(M1, a.LOW)
    a.digitalWrite(M2, a.LOW)
    a.analogWrite(E1, 0)
    a.analogWrite(E2, 0)
    
def right(valueR,valueL):
    a.digitalWrite(M1, a.LOW)
    a.digitalWrite(M2, a.HIGH)
    a.analogWrite(E1, a.valueR)
    a.analogWrite(E2, a.valueL)

def left(valueR,valueL):
    a.digitalWrite(M1, a.HIGH)
    a.digitalWrite(M2, a.LOW)
    a.analogWrite(E1, a.valueR)
    a.analogWrite(E2, a.valueL)
    

if ((sensorR == 1) && (sensorL == 1)):
    forward(70,70)

elif ((sensorR == 0) && (sensorL == 1)):
    right(255,225)

elif ((sensorR == 1) && (sensorL == 1)):
    left(225,255)

elif ((sensorR == 1) && (sensorL == 1)):
    stop(0,0)


    

elif ((sensorR == 1) && (sensorL == 1))
