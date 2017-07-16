#! /usr/bin/env python
from time import sleep

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO")

GPIO.setmode(GPIO.BOARD)

outputList = [36,37,38,40]

GPIO.setup(outputList,GPIO.OUT)

for j in range(0,20):
    print("{} cycle".format(j))
    for i in outputList:
        GPIO.output(i,GPIO.LOW)
        print("{}:LOW".format(i))
        sleep(0.03)
    for i in outputList:
        GPIO.output(i,GPIO.HIGH)
        print ("{}:HIGH".format(i))
        sleep(0.03)

GPIO.cleanup()