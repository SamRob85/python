num=int(input("Decimal"))
digit1=0
digit2=0
digit3=0

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
print "Lights and sound on"
if(digit1==1):
	GPIO.output(18, GPIO.HIGH)
if(digit2==1):
	GPIO.output(24, GPIO.HIGH)
if(digit3==1):
	GPIO.output(22, GPIO.HIGH)

time.sleep(10)

GPIO.output(18, GPIO.LOW)
GPIO.output(24, GPIO.LOW)
GPIO.output(22, GPIO.LOW)
GPIO.cleanup()
