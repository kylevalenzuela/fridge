import RPi.GPIO as GPIO #import the GPIO library  
import time

GPIO.setmode(GPIO.BOARD)  
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

name = "Kyle"  
print("Hello " + name)

while True:  
    if GPIO.input(23):
       print("Door is open")
       time.sleep(2)
    else:
       print("Door is closed")
       time.sleep(2)