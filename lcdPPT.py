
import RPi.GPIO as GPIO
import time

# Define GPIO to LCD mapping
LCD_RS = 7
LCD_E  = 8
LCD_D4 = 25 
LCD_D5 = 24
LCD_D6 = 23
LCD_D7 = 18

# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True   # mode = True  for character
                 # False for command
LCD_CMD = False

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line 

# Timing constants
E_PULSE = 0.00005
E_DELAY = 0.00005

def main():
  # Main program block

  GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
  GPIO.setup(LCD_E, GPIO.OUT)  # E
  GPIO.setup(LCD_RS, GPIO.OUT) # RS
  GPIO.setup(LCD_D4, GPIO.OUT) # DB4
  GPIO.setup(LCD_D5, GPIO.OUT) # DB5
  GPIO.setup(LCD_D6, GPIO.OUT) # DB6
  GPIO.setup(LCD_D7, GPIO.OUT) # DB7

  # Initialise display
  lcd_init()

  # Send some test by EN = true and after sending data EN = false
  lcd_byte(LCD_LINE_1, LCD_CMD)  #LCD_CMD = false

  # this function store string upto 16 char and pass to lcd_byte() function
  lcd_string("Rasbperry Pi")
  lcd_byte(LCD_LINE_2, LCD_CMD)
  lcd_string("Model B")

  time.sleep(3) # 3 second delay

  # Send some text
  lcd_byte(LCD_LINE_1, LCD_CMD)
  lcd_string("Robodia")
  lcd_byte(LCD_LINE_2, LCD_CMD)
  lcd_string("Bhopal")

  time.sleep(20)

def lcd_init():
  # Initialise display by passing some hex commands
  lcd_byte(0x33, LCD_CMD)  # 8-bit 1st line
  lcd_byte(0x32, LCD_CMD)  # 
  lcd_byte(0x28, LCD_CMD)  # 4-bit 2nd line
  lcd_byte(0x0C, LCD_CMD)  # display on cursor off
  lcd_byte(0x06, LCD_CMD)  # entry mode
  lcd_byte(0x01, LCD_CMD)  # clear display

def lcd_string(message):
  # Send string to display

  message = message.ljust(LCD_WIDTH, " ")  #LCD_WIDTH = 16 

  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]), LCD_CHR)   #LCD_CHR = true

def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command

  GPIO.output(LCD_RS, mode) # RS

  # High bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits & 0x10 == 0x10:     #0x10 = b00010000
    GPIO.output(LCD_D4, True)
  if bits & 0x20 == 0x20:     #0x20 = b00100000
    GPIO.output(LCD_D5, True)
  if bits & 0x40 == 0x40:     #0x40 = b01000000
    GPIO.output(LCD_D6, True)
  if bits & 0x80 == 0x80:     #0x80 = b10000000
    GPIO.output(LCD_D7, True)

  # Toggle 'Enable' pin
  time.sleep(E_DELAY)    
  GPIO.output(LCD_E, True)    #EN = true   to send data available on D4 - D7  
  time.sleep(E_PULSE)         #delay for pulse
  GPIO.output(LCD_E, False)   #EN = false
  time.sleep(E_DELAY)      

  # Low bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x01==0x01:
    GPIO.output(LCD_D4, True)
  if bits&0x02==0x02:
    GPIO.output(LCD_D5, True)
  if bits&0x04==0x04:
    GPIO.output(LCD_D6, True)
  if bits&0x08==0x08:
    GPIO.output(LCD_D7, True)
  # Toggle 'Enable' pin
  time.sleep(E_DELAY)    
  GPIO.output(LCD_E, True)  
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)  
  time.sleep(E_DELAY)   
if __name__ == '__main__':
  main()