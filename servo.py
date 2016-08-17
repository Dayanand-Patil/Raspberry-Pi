import os
import time
import Rpi.GPIO as GPIO
Pwm_pin = 21
Led_pin  =  23 
Button_pin = 17
Duty = 50

GPIO.setmode(GPIO.BCM)
GPIO.setup(Pwm_pin, GPIO.OUT)    # Pwm_pin as output
GPIO.setup(Led_pin, GPIO.OUT)     #led_pin as output
GPIO.setup(Button_pin, GPIO.IN)    # Button pin as input
Pwm = GPIO.PWM(Pwm_pin, 50)       # set pwm val = 50
GPIO.output(Led_pin, GPIO.LOW)    # initially led pin = low
Pwm.start(duty)                   # start the pwm
Try:
      while 1:
               if GPIO.input(Led_pin) :        #
                      Pwm.ChangeDutyCycle(duty)
                       GPIO.output(ledPin, GPIO.LOW)
                else: # button is pressed:
                        pwm.ChangeDutyCycle(100-dc)
                        GPIO.output(ledPin, GPIO.HIGH)
                        time.sleep(0.075)
                        GPIO.output(ledPin, GPIO.LOW)
                        time.sleep(0.075)
      except KeyboardInterrupt :     # If CTRL+C is pressed, exit cleanly:
pwm.stop()     # stop PWM
GPIO.cleanup()   # cleanup all GPIO

                    
