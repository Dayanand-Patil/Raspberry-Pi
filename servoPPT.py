import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP)
P = GPIO.PWM(3, 100)
P.start(0)

while 1:
        #       angle = int(input("Enter servo angle u want to move : "))
        if GPIO.input(4):
                print "----------------"
                for i in range(0, 100, 10):
                        print "F/W :",i
                        P.ChangeDutyCycle(i)
                        GPIO.output(2, 1)
                        time.sleep(1)
        else :
                print "-----------------"
                for i in range (100, 0, -10) :
                        print "R/W :",i
                        P.ChangeDutyCycle(i)
                        GPIO.output(2, 0)
                        time.sleep(1)


