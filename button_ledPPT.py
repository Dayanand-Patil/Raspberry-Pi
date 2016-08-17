import RPi.GPIO as GPIO
 # Use the pin numbers from the ribbon cable board
GPIO.setmode(GPIO.BCM)
 # Set up this pin as input.
GPIO.setup(18, GPIO.IN)
  #Set up led pin as output
 GPIO.setup(17, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
 # Check the value of the input pin
GPIO.input(18)
 # Hold down the button, run the command again. The output should be "true".
GPIO.input(18)
input = True
prev_input = True

input = GPIO.input(18)

if (prev_input and (not input)) :
	print("Button pressed")
            if(input == True)
                print “led is ON”
                GPIO.out(17, HIGH)
                GPIO.out(23, LOW)
                       
else :
    GPIO.out(17, LOW)
    GPIO.out(23, HIGH)
#update previous input
prev_input  =  input

#slight pause to debounce
	time.sleep(0.05)
	
