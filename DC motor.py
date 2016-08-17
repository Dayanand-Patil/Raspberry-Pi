

# Import required libraries
import RPi.GPIO as GPIO
import sys
import time

# Tell GPIO library to use GPIO references
GPIO.setmode(GPIO.BCM)

# List of LED GPIO Array
Forw=[17,27]
Back=[18,22]
Left=[18,27]
Right=[17,22]

def Choose():
#	GPIO.cleanup()
	Command = raw_input("1=Forward\n2=Backward\n3=Left\n4=Right\n5=Stop\n")
	if Command == "1":
		Forward()
	elif Command == "2":
		Backward()
	elif Command == "3":
		Left1()
	elif Command == "4":
		Right1()
        elif Command == "5":
               Stop()    
	else:
		Choose()


def Forward():
#	Clean()
	for x in range(2):
		GPIO.setup(Forw[x], GPIO.OUT)
		GPIO.output(Forw[x], False)
		GPIO.output(Forw[x], True)
	time.sleep(0.2)
#	Clean()
	Choose()

def Backward():
#	Clean()
	for x in range(2):
		GPIO.setup(Back[x], GPIO.OUT)
		GPIO.output(Back[x], False)
		GPIO.output(Back[x], True)
	time.sleep(0.2)
#	Clean()
	Choose()
		
def Left1():
#	Clean()
	for x in range(2):
		GPIO.setup(Left[x], GPIO.OUT)
		GPIO.output(Left[x], False)
		GPIO.output(Left[x], True)
	time.sleep(0.2)
#	Clean()
	Choose()
		
def Right1():
#	Clean()
	for x in range(2):
		GPIO.setup(Right[x], GPIO.OUT)
		GPIO.output(Right[x], False)
		GPIO.output(Right[x], True)
	time.sleep(0.2)
#	Clean()
	Choose()

def Stop():
      GPIO.cleanup()
#       Clean() 
      Choose()
		
def Clean():
	GPIO.cleanup()

     #    Clean()
Choose()
