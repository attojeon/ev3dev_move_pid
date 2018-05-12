from time   import sleep
from random import choice, randint

from ev3dev.auto import *

motorB = LargeMotor('outB')
motorC = LargeMotor('outC')

motorB.run_forever(speed_sp = 0)
motorC.run_forever(speed_sp = 0)

Sound.beep()