import RPi.GPIO as GPIO
from time import sleep
RELAY_PIN = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN,GPIO.OUT)
GPIO.output(RELAY_PIN,1)
