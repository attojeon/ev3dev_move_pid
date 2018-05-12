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
sensorAvg = 40
defaultSpeed = 300
prevError = 0
curError = 0
val = 0
Kp = 10
Ki = 0.05
incError = 0.0
leftspd = 0.0
rightspd = 0.0

while btn.backspace == False :
    val = sensorColor.value() 
    curError = val - sensorAvg
    incError = incError + curError 
    oKp = curError * Kp
    oKi = incError * Ki

    leftSpd = defaultSpeed + (oKp + oKi)
    rightSpd = defaultSpeed - (oKp + oKi)

    if(leftSpd < -999) : leftSpd = -999
    if(rightSpd < -999) : rightSpd = -999
    if(leftSpd > 999 ) : leftSpd = 999
    if(rightSpd > 999 ) : rightSpd = 999
    print("TR:{}, L:{}, R:{}".format( (oKp+oKi), leftSpd, rightSpd) )
    setSpeed( leftSpd, rightSpd )

    
stop()
Sound.beep()


