import RPi.GPIO as GPIO
import time

led_pin = 22

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(led_pin,GPIO.OUT)

while True:
    GPIO.output(led_pin,True)
    time.sleep(5)
    GPIO.output(led_pin,False)
    time.sleep(5)