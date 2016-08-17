
import time
import RPi.GPIO as GPIO
 
# RGB LED Module (TEST)
 
#Setup Active states
#Common Cathode RGB-LEDs (Cathode=Active Low)
LED_ENABLE = 0
LED_DISABLE = 1
RGB_ENABLE = 1
RGB_DISABLE = 0
 
#LED CONFIG - Set GPIO Ports
LED1 = 12   #B4
LED2 = 16   #B18
LED3 = 18   #B23
LED4 = 22   #B24
LED5 = 7    #B25
LED = [LED1,LED2,LED3,LED4,LED5]
RGB_RED = 11   #B22
RGB_GREEN = 13 #B21 Rev1  B27 Rev2
RGB_BLUE = 15  #B17
RGB = [RGB_RED,RGB_GREEN,RGB_BLUE]
 
def led_setup():
  #Set up the wiring
  GPIO.setmode(GPIO.BOARD)
  # Setup Ports
  for val in LED:
    GPIO.setup(val, GPIO.OUT)
  for val in RGB:
    GPIO.setup(val, GPIO.OUT)
 
def led_activate(led,colour):
  GPIO.output(led,LED_ENABLE)
  GPIO.output(colour,RGB_ENABLE)
 
def led_deactivate(led,colour):
  GPIO.output(led,LED_DISABLE)
  GPIO.output(colour,RGB_DISABLE)
 
def led_clear():
  for val in LED:
    GPIO.output(val, LED_DISABLE)
  for val in RGB:
    GPIO.output(val, RGB_DISABLE)
 
def main():
  led_setup()
  led_clear()
  led_activate(LED1,RGB_RED)
  time.sleep(5)
  led_deactivate(LED1,RGB_RED)
  led_clear()
  GPIO.cleanup()
 
main()
#End