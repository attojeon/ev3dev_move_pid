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

def setSpeed(left, right):
    motorB.run_forever(speed_sp = left)
    motorC.run_forever(speed_sp = right)

motorB = LargeMotor('outB')
motorC = LargeMotor('outC')
sensorColor = ColorSensor()
sensorColor.mde = 'COL-REFLECT'
sensorAvg = 40
defaultSpeed = 300
err = 0
val = 0
Kp = 10

while btn.backspace == False :
    val = sensorColor.value()
    error = val - sensorAvg
    leftSpd = defaultSpeed + error * Kp
    rightSpd = defaultSpeed - error * Kp
    setSpeed( leftSpd, rightSpd )
    print("L:{}, R:{}".format(leftSpd, rightSpd))
    

stop()
Sound.beep()


