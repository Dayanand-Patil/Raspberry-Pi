import RPi.GPIO as GPIO
import time

pinRS = 7
pinE = 8
pinData = [4, 17, 27, 22, 25, 24, 23, 18]

def setPins(binaryInput):
	#Sets the values for each of the data pins based on the input received ->
	for i in range(0, len(binaryInput)):
		if binaryInput[i] == "1":
			GPIO.output(pinData[i], True)
			
		else:
			GPIO.output(pinData[i], False)
	#Sending pin E high then low reads the data into the LCD screen		
	time.sleep(0.01)
	GPIO.output(pinE, True)
	time.sleep(0.01)
	GPIO.output(pinE, False)	
	time.sleep(0.01)
	
def setControlPins(number):
	binaryNumber = bin(number)[2:]
	while len(binaryNumber) < 8:
		binaryNumber = "0" + binaryNumber #Adds leading zeros to make an 8-bit binary string
	
	GPIO.output(pinRS, False) #Setting RS pin to False tells the LCD that data received is for control inputs	
	setPins(binaryNumber[::-1]) #Reverses the order of the binary number so it matches the pin layout

def writeText(text, line):
	if line == 1:
		setControlPins(128) #Writes onto Line 1 (80 in hex)
	else:
		setControlPins(192) #Writes onto Line 2 (C0 in hex)
	
	GPIO.output(pinRS, True) #Setting RS pin to True tells the LCD that data received is for display
	
	while len(text) < 16:
		text = " " + text + " " #Centring the text on the screen
	
	for c in text: #Loops through each character in the text string
		binaryLetter = bin(int(ord(c)))[2:] #Gets the binary value of the character
		while len(binaryLetter) < 8:
			binaryLetter = "0" + binaryLetter
		setPins(binaryLetter[::-1])
			
def initialiseLCD():
	GPIO.setmode(GPIO.BCM) #Use Raspberry's GPIO numbering
	#Set all pins to output mode ->
	GPIO.setup(pinRS, GPIO.OUT)  
	GPIO.setup(pinE, GPIO.OUT)
	for i in pinData:
		GPIO.setup(i, GPIO.OUT)

	#Initialise all pins (set to false) ->	
	GPIO.output(pinRS, False)
	GPIO.output(pinE, False)
	for i in pinData:
		GPIO.output(i, False)
	
	#Read in the number 38 in hex (56 decimal) sets interface to 8-bit mode with 2 lines-> 
	setControlPins(56)

	#Read in the number 1 in hex/decimal clears the display-> 
	setControlPins(1)
	
	#Read in the number 0C in hex (12 in decimal) sets display on with cursor off -> 
	setControlPins(12)
	
	#Read in the number 6 in hex sets the display to entry mode
	setControlPins(6)
	
	#Useful guide to commands: http://www.8051projects.net/lcd-interfacing/commands.php

initialiseLCD()

writeText("Made by", 1) #Writes text onto line 1
writeText("@GeekyNicki", 2) #Writes text onto line 2

time.sleep(10) #Displays the text for 10 seconds