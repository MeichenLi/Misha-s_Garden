import RPi.GPIO as  GPIO
import time

pin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.IN)

def callback(pin):
    if GPIO.input(pin):
        print("dry") # no water,big resistance, value = 1
        time.sleep(1)
    else:
        print("watery")
        time.sleep(1)

GPIO.add_event_detect(pin,GPIO.BOTH,bouncetime=300)
GPIO.add_event_callback(pin,callback)

while True:
    time.sleep(1)
