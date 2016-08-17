import spidev
import time

channel = 0
spi = spidev.SpiDev()
spi.open(0, 0)     
#If you had the pot on CH1 and connected to GPIO 7 (SPIO_CE1_H)
#then you would have code - spi.open(1, 1). 
#And so if you wanted to get info from any other channel 
#from 2 to 7 the second digit in the list correspond to that channel number.

while True:
    result = spi.xfer2([1, (8 + channel) << 4, 0])    
    digital_code = int(((result[1] & 3) << 8) + result[2])
    voltage = round(((digital_code * 3.33) / 1024), 2)
    print voltage
    time.sleep(0.5)
