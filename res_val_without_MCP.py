import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
a_pin = 18
b_pin = 23

def discharge():
    GPIO.setup(a_pin, GPIO.IN)   # pin a in
    GPIO.setup(b_pin, GPIO.OUT)  # b out
    GPIO.output(b_pin, False)    # b low
    time.sleep(0.005)

def charge_time():
    GPIO.setup(b_pin, GPIO.IN)   # b in
    GPIO.setup(a_pin, GPIO.OUT)   # a out
    count = 0
    GPIO.output(a_pin, True)     # a high
    
    while not GPIO.input(b_pin):   # check state change than prev.
    count = count + 1
    return count                  # count and ret

def analog_read():
    discharge()
    return charge_time()
   
    while True:
       print(analog_read())       # it print charge time value 
       time.sleep(1)