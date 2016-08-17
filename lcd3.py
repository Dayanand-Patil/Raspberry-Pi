
import RPi.GPIO as GPIO
import time

LCD_RS = 22
LCD_E  = 4
LCD_D4 = 25
LCD_D5 = 24
LCD_D6 = 23
LCD_D7 = 18

LCD_WIDTH = 16      # Maximum characters per line
LCD_CHR = True      # Register Select to Accept Characters
LCD_CMD = False     # Register Select to Accept Commands

LCD_LINE_1 = 0x80   # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0   # LCD RAM address for the 2nd line
LCD_LINE_3 = 0x94   # LCD RAM address for the 3rd line
LCD_LINE_4 = 0xD4   # LCD RAM address for the 4th line

E_PULSE = 0.00005
E_DELAY = 0.00005

LINE_1_16x2 = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 
        0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F]
LINE_2_16x2 = [0x40, 0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48, 
        0x49, 0x4A, 0x4B, 0x4C, 0x4D, 0x4E, 0x4F]

LINE_1_20x4 = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 
        0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10, 0x11, 
        0x12, 0x13]
LINE_2_20x4 = [0x40, 0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48, 
        0x49, 0x4A, 0x4B, 0x4C, 0x4D, 0x4E, 0x4F, 0x50, 0x51, 
        0x52, 0x53]
LINE_3_20x4 = [0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1A, 0x1B, 0x1C, 
        0x1D, 0x1E, 0x1F, 0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 
        0x26, 0x27]
LINE_4_20x4 = [0x54, 0x55, 0x56, 0x57, 0x58, 0x59, 0x5A, 0x5b, 0x5C, 
        0x5D, 0x5E, 0x5F, 0x60, 0x61, 0x62, 0x63, 0x64, 0x65, 
        0x66, 0x67]



def set_gpio():
     GPIO.setwarnings(False)
     GPIO.setmode(GPIO.BCM)          # Use BCM GPIO numbers
     GPIO.setup(LCD_E, GPIO.OUT)     # E
     GPIO.setup(LCD_RS, GPIO.OUT)    # RS
     GPIO.setup(LCD_D4, GPIO.OUT)    # DB4
     GPIO.setup(LCD_D5, GPIO.OUT)    # DB5
     GPIO.setup(LCD_D6, GPIO.OUT)    # DB6
     GPIO.setup(LCD_D7, GPIO.OUT)    # DB7

def lcd_init():
    send_data(0x30, LCD_CMD)    # Initialize
    send_data(0x28, LCD_CMD)    # Set 4-bit mode, 2 line, 5x7 matrix
    send_data(0x0F, LCD_CMD)    # Display On, set cursor underling and blinking
    send_data(0x06, LCD_CMD)    # Character entry increment, Display shift off
    send_data(0x01, LCD_CMD)    # Clear Screen


def send_data(instr, rs_mode):
    # Send byte to data pins
    # instr = data set to send
    # rs_mode = Register Select :
    #               True  for character
    #               False for command

    GPIO.output(LCD_RS, rs_mode)

    set_data_pins()             # Reset pins to False
    send_data_to_pins('high', instr)
    commit_data()
    set_data_pins()             # Reset pins to False
    send_data_to_pins('low', instr)
    commit_data()


def set_data_pins():
    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)


def send_data_to_pins(state, nibble):
    if state == 'high':
        if nibble & 0x10 == 0x10:
            GPIO.output(LCD_D4, True)
        if nibble & 0x20 == 0x20:
            GPIO.output(LCD_D5, True)
        if nibble & 0x40 == 0x40:
            GPIO.output(LCD_D6, True)
        if nibble & 0x80 == 0x80:
            GPIO.output(LCD_D7, True)
    elif state == 'low':
        if nibble & 0x01 == 0x01:
            GPIO.output(LCD_D4, True)
        if nibble & 0x02 == 0x02:
            GPIO.output(LCD_D5, True)
        if nibble & 0x04 == 0x04:
            GPIO.output(LCD_D6, True)
        if nibble & 0x08 == 0x08:
            GPIO.output(LCD_D7, True)


def commit_data():
    time.sleep(E_DELAY)
    GPIO.output(LCD_E, True)
    time.sleep(E_PULSE)
    GPIO.output(LCD_E, False)
    time.sleep(E_DELAY)     

def set_line(line_number):
    if line_number == 1:
        send_data(LCD_LINE_1, LCD_CMD)
    elif line_number == 2:
        send_data(LCD_LINE_2, LCD_CMD)
    elif line_number == 3:
        send_data(LCD_LINE_3, LCD_CMD)
    elif line_number == 4:
        send_data(LCD_LINE_4, LCD_CMD)


def lcd_string(message, line_number):
    set_line(line_number)

    message = message.ljust(LCD_WIDTH, " ")

    for i in range(LCD_WIDTH):
        send_data(ord(message[i]), LCD_CHR)

#################################################################
set_gpio()
lcd_init()
scroll_text()

lcd_string("Hello", 1)
lcd_string("World", 2)


