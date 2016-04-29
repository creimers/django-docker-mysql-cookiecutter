import requests

def check(pin):
    try:
        response = requests.get('http://localhost:8000')
    except:
        response = None
    
    if response and response.status_code == 200:
        try:
            import RPi.GPIO as GPIO
            import time
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(pin, GPIO.OUT)

            GPIO.output(pin, True)
        except:
            pass

    else:
        try:
            import RPi.GPIO as GPIO
            import time
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(pin, GPIO.OUT)

            GPIO.output(pin, False)
        except:
            pass

if __name__ == '__main__':
    check(27)
