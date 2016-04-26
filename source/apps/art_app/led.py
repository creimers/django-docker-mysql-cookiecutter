try:
    import RPi.GPIO as GPIO
    import time
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)

    def blink(pin):
        GPIO.output(pin, True)
        time.sleep(0.1)
        GPIO.output(pin, False)


except:

    def blink(pin):
        print('blinking pin %s' % pin)
