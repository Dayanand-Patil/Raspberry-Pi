import RPi.GPIO as GPIO     # imports Raspberry Pi's GPIO module
 import time 			 	# imports time module
 enable_pin = 18
 in1_pin = 17
 int_pin = 27
 GPIO.setmode(GPIO.BCM) 		# sets GPIO pins naming same as BCM SoC
 GPIO.setup(enable_pin, GPIO.OUT)	# sets pin 18  as output
 GPIO.setup(in2_pin, GPIO.OUT) 	 	# sets pin 24  as output
 pwm = GPIO.PWM(enable_pin, 500) 	# create PWM with enable_pin as channel
                                    # & frequency 500

 pwm.start(0) 	# to start PWM with duty cycle 0


 def clockwise():
	GPIO.output(in1_pin, True) 	# true sets the pin high
	GPIO.output(in2_pin, False) 	# false sets the pin low

 def counter_clockwise():
	GPIO.output(in1_pin, False) 	# true sets the pin high
	GPIO.output(in2_pin, True) 	# false sets the pin low

 while True:
	cmd = raw_input("Command, f/r 0..9, E.g. f5 :")	#input data
	direction = cmd[0] 		# check for direction parameter
	if direction == "f":
		clockwise()
	else:
		counter_clockwise()
	speed = int(cmd[1]) * 10 	#create speed parameter
	pwm.ChangeDutyCycle(speed) 	# change pwm duty cycle
