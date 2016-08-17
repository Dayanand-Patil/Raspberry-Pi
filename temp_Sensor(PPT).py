 
import spidev
import time
import os
 
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
 
# Function to read SPI data from MCP3008 chip  Channel must be an integer 0-7
def ReadChannel(channel):
     adc = spi.xfer2([1,(8+channel)<<4,0])
     data = ((adc[1]&3) << 8) + adc[2]
     return data
 
# Function to convert data to voltage level, rounded to specified number of decimal places.
def ConvertVolts(data,places ):
     volts = (data * 3.3) / float(1023)
     volts = round(volts,places)
     return volts
 
# Function to calculate temperature from TMP36 data, rounded to specified
# number of decimal places.
def ConvertTemp (data, places):
       # don't use 50 calibration bcz it gives -ve value of temp
      # temp = ((data * 330)/float(1023))-50 
       temp = ((data * 330)/float(1023))
       temp = round (temp, places)
       return temp
 
       temp_channel  = 0     # Define sensor channels
 
       delay = 5      # Define delay between readings

 
while True:
 
      # Read the temperature sensor data
      temp_level = ReadChannel (temp_channel)
      temp_volts = ConvertVolts (temp_level, 2)
      temp       = ConvertTemp (temp_level, 2)
 
      # Print out results
      print "--------------------------------------------"
      print("Temp : {} ({}V) {} deg C".format(temp_level,temp_volts, temp))
 
      # Wait before repeating loop
      time.sleep(delay)

