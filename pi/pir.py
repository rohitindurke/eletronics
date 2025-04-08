import RPi.GPIO as GPIO
import time

led_pin = 22
pir_pin = 23

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(led_pin,GPIO.OUT)
GPIO.setup(pir_pin,GPIO.IN)

while True:
    if(GPIO.input(pir_pin)):
        GPIO.output(led_pin,True)
    else:
        GPIO.output(led_pin,False)
    time.sleep(5)