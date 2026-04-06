import RPi.GPIO as GPIO

RELAY_1 = 18
RELAY_2 = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_1, GPIO.OUT)
GPIO.setup(RELAY_2, GPIO.OUT)

def turn_on():
    GPIO.output(RELAY_1, GPIO.HIGH)
    GPIO.output(RELAY_2, GPIO.HIGH)

def turn_off():
    GPIO.output(RELAY_1, GPIO.LOW)
    GPIO.output(RELAY_2, GPIO.LOW)

def cleanup():
    GPIO.cleanup()
