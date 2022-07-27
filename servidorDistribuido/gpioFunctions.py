import RPi.GPIO as GPIO

def acendeLeds(leds):
    GPIO.output(leds, GPIO.HIGH)

def apagaLeds(leds):
    GPIO.output(leds, GPIO.LOW)