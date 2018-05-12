from time   import sleep
from random import choice, randint

from ev3dev.auto import *

motorB = LargeMotor('outB')
motorC = LargeMotor('outC')
sensorColor = ColorSensor()
sensorColor.mde = 'COL-REFLECT'
btn = Button()
colorvalue = []

def stop():
    motorB.run_forever(speed_sp = 0)
    motorC.run_forever(speed_sp = 0)

def move(spd):
    motorB.run_forever(speed_sp = spd)
    motorC.run_forever(speed_sp = spd)

while btn.backspace == False :
    val = sensorColor.value()
    colorvalue.append( val )
    print( val )
    move(400)
    sleep(0.001)

stop()
Sound.beep()

min = 100
max = 0
sum = 0
avg = 0.0
for v in colorvalue:
    if( v < min ) :
        min = v
    if( v > max ) :
        max = v
    sum = sum + v
    
avg = ( max + min) / 2 

print( 'max value : {}'.format( max ))
print( 'min value : {}'.format( min ))
print( 'avg value : {}'.format( avg ))

    
