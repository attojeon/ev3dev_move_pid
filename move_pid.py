from time   import sleep
from random import choice, randint
from ev3dev.auto import *

motorB = LargeMotor('outB')
motorC = LargeMotor('outC')
sensorColor = ColorSensor()
sensorColor.mode = 'COL-REFLECT'
btn = Button()


def stop():
    motorB.run_forever(speed_sp = 0)
    motorC.run_forever(speed_sp = 0)

def setSpeed(leftspd, rightspd):
    motorB.run_forever(speed_sp = leftspd)
    motorC.run_forever(speed_sp = rightspd)

motorB = LargeMotor('outB')
motorC = LargeMotor('outC')
sensorColor = ColorSensor()
sensorColor.mde = 'COL-REFLECT'
sensorAvg = 35
defaultSpeed = 500
prevError = 0
curError = 0
val = 0
#Ks = [10.0, 0.01, 10.0] : Good
Ks = [9.0, 0.02, 25.0]
Kp = Ks[0]
Ki = Ks[1]
Kd = Ks[2]
incError = 0.0
leftspd = 0.0
rightspd = 0.0
prevError = 0.0
curError = 0.0

while btn.backspace == False :
    val = sensorColor.value() 
    curError = val - sensorAvg
    incError = incError + curError 
    oKp = curError * Kp
    oKi = incError * Ki
    oKd = (curError - prevError) * Kd

    leftSpd = defaultSpeed + (oKp + oKi + oKd)
    rightSpd = defaultSpeed - (oKp + oKi + oKd)

    if(leftSpd < -999) : leftSpd = -999
    if(rightSpd < -999) : rightSpd = -999
    if(leftSpd > 999 ) : leftSpd = 999
    if(rightSpd > 999 ) : rightSpd = 999
    print("oki:{},\t okd:{},\t TR:{},\t L:{},\t R:{}".format(oKi, oKd, (oKp+oKi+oKd), leftSpd, rightSpd) )
    setSpeed( leftSpd, rightSpd )
    prevError = curError
    #sleep(0.001)

    
stop()
Sound.beep()


