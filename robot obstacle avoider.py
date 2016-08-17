
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN) #Right IR sensor module
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Activation button
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Left IR sensor module
GPIO.setup(5, GPIO.OUT)  #Left motor control   IN1
GPIO.setup(7, GPIO.OUT)  #Left motor control   IN2
GPIO.setup(11, GPIO.OUT) #Right motor control  IN3
GPIO.setup(13, GPIO.OUT) #Right motor control  IN4

#Motor stop/brake
GPIO.output(5, 0) 
GPIO.output(7, 0)
GPIO.output(11, 0)
GPIO.output(13, 0)

flag = 0
while True:
	button_state = GPIO.input(12) # pin 12 as i/p check state of button
	if button_state == 1: #Robot is activated when button is pressed
		flag = 1
		print "Robot Activated",left_ir
	
	while flag == 1:
		right_ir = GPIO.input(3)  #Listening for output from right IR sensor
		left_ir  = GPIO.input(16)  #Listening for output from left IR sensor
		
		if right_ir == 0: #Obstacle detected on right IR sensor
			print "Obstacle detected on Right",right_ir 
			#Move in reverse direction
			GPIO.output(5, 1) #Left motor turns anticlockwise
			GPIO.output(7, 0)  
			GPIO.output(11, 1) #Right motor turns clockwise
			GPIO.output(13, 0)		
			time.sleep(1)

			#Turn robot left
			GPIO.output(5, 0) #Left motor turns clockwise
			GPIO.output(7, 1)
			GPIO.output(11, 1) #Right motor turns clockwise
			GPIO.output(13, 0)
			time.sleep(2)

		if left_ir == 0: #Obstacle detected on left IR sensor
			print "Obstacle detected on Left",left_ir
			GPIO.output(5, 1)    #left anti..
			GPIO.output(7, 0)
			GPIO.output(11, 1)   # right clock
			GPIO.output(13, 0)		
			time.sleep(1)

			GPIO.output(5, 1)     #left anti..
			GPIO.output(7, 0)
			GPIO.output(11, 0)    #right anti..
			GPIO.output(13, 1)
			time.sleep(2)

		elif right_ir == 0 and left_ir == 0:
			print "Obstacles on both sides"
			GPIO.output(5, 1)   #
 			GPIO.output(7, 0)
			GPIO.output(11, 1)
			GPIO.output(13, 0)		
			time.sleep(2)

			GPIO.output(5, 1)
			GPIO.output(7, 0)
			GPIO.output(11, 0)
			GPIO.output(13, 1)
			time.sleep(4)
			
		elif right_ir == 1 and left_ir == 1:	#No obstacles, robot moves forward
			print "No obstacles", right_ir
			#Robot moves forward
			GPIO.output(5, 0)
			GPIO.output(7, 1)
			GPIO.output(11, 0)
			GPIO.output(13, 1)
			time.sleep(0.5)
		button_state = GPIO.input(12)
		if button_state == 1: #De activate robot on pushin the button
			flag = 0
			print "Robot De-Activated",j
			GPIO.output(5, 0)
			GPIO.output(7, 0)
			GPIO.output(11, 0)
			GPIO.output(13, 0)
			time.sleep(1)
		


	