import os 
import time
import Rpi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
Count = 0

def  buzzer_loop ( ) :
         # dot dot dot
        GPIO.output(22, GPIO.HIGH)
         time.sleep(.1)
         GPIO.output(22, GPIO.LOW)
         time.sleep(.1)
         GPIO.output(22, GPIO.HIGH)
         time.sleep(.1)
         GPIO.output(22, GPIO.LOW)
         time.sleep(.1)
         GPIO.output(22, GPIO.HIGH)
         time.sleep(.1)
         GPIO.output(22, GPIO.LOW)
         time.sleep(.1)
         # dash dash dash
        GPIO.output(22, GPIO.HIGH)
         time.sleep(.2)
         GPIO.output(22, GPIO.LOW)
         time.sleep(.2)
         GPIO.output(22, GPIO.HIGH)
         time.sleep(.2)
         GPIO.output(22, GPIO.LOW)
         time.sleep(.2)
         GPIO.output(22, GPIO.HIGH)
         time.sleep(.1)
         GPIO.output(22, GPIO.LOW)
         time.sleep(.1)

os.system(‘clear’)
print “…..buzzer code……”
count = input(“how many times would you like to run loop? : ”)
while (count > 0) :
      buzzer_loop()
      count = count -1
time.sleep(1)

