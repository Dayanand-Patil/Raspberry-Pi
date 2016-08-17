
import sys
import wiringpi2
from time import sleep

gpio = wiringpi2.GPIO(wiringpi2.GPIO.WPI_MODE_GPIO)
enable_1 = 27
enable_2 = 17
enable_3 = 18

gpio.pinMode(enable_1,gpio.INPUT)
gpio.pinMode(enable_2,gpio.OUTPUT)
gpio.pinMode(enable_3,gpio.OUTPUT)
gpio.pullUpDnControl(enable_1,1)
gpio.pinMode(enable_2,1)
gpio.pinMode(enable_3,1)

gpio.digitalWrite(enable_2,gpio.HIGH)
gpio.digitalWrite(enable_3,gpio.LOW)
sleep (0.1)
gpio.digitalWrite(enable_2,gpio.HIGH)
gpio.digitalWrite(enable_3,gpio.HIGH)

samples = [0 for i in xrange(50)]

j=0
ons = 0;

while (1):
        sample = gpio.digitalRead(enable_1)
        samples[j] = sample
        ons = 0;
        for i in xrange(50):
                if (samples[i] >0):
                        ons = ons +1;
        j = j + 1
        if (j>49):
                j=0
                print ons
        if ons >25:
                print ons
                gpio.digitalWrite(enable_2,gpio.LOW)
                gpio.digitalWrite(enable_3,gpio.HIGH)
                sleep (0.1)
                gpio.digitalWrite(enable_2,gpio.HIGH)
                gpio.digitalWrite(enable_3,gpio.HIGH)
                sleep (2)
                gpio.digitalWrite(enable_2,gpio.HIGH)
                gpio.digitalWrite(enable_3,gpio.LOW)
                sleep (0.1)
                gpio.digitalWrite(enable_2,gpio.HIGH)
                gpio.digitalWrite(enable_3,gpio.HIGH)
                for i in xrange(50):
                        samples[i] = 0;
                sleep (0.01)