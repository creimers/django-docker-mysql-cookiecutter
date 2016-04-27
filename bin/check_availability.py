import requests

def check(pin):
    try:
        import RPi.GPIO as GPIO
        import time
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)

        response = requests.get('http://localhost:8000')
        if response.status_code == 200:
            GPIO.output(pin, True)
        else:
            GPIO.output(pin, False)

    except:
        pass

if __name__ == '__main__':
    check(18)
