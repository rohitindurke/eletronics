
import RPi.GPIO as GPIO
import time

Led_pin = 22
switch_pin = 23

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(Led_pin,GPIO.OUT)
GPIO.setup(switch_pin,GPIO.IN)

while True:
    if GPIO.input(switch_pin):
        GPIO.output(Led_pin,True)
    else:
        GPIO.output(Led_pin,False)
    time.sleep(5)

