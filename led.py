import RPi.GPIO as GPIO
import time

# do the initial setup
GPIO.cleanup()
 GPIO.setmode(GPIO.BCM) # to use Raspberry Pi board pin numbers
  GPIO.setup(11, GPIO.OUT) # set up GPIO output channel
 
  # start to blink LED
GPIO.output(11, GPIO.LOW) # set RPi board pin 11 low. Turn off LED.
 time.sleep(1)       # delay of 1 sec.
 GPIO.output(11, GPIO.HIGH) # set RPi board pin 11 high. Turn on LED.
  time.sleep(2)
