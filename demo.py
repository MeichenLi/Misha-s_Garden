import RPi.GPIO as  GPIO
import time

channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN)

def callback(channel):
    if GPIO.input(channel):
        print("Null")
    else:
        print("water")

GPIO.add_event_detect(channel,GPIO.BOTH,bouncetime=300)
GPIO.add_event_callback(channel,callback)
while(1):
    time.slepp(1)