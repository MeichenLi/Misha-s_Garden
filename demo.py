import RPi.GPIO as GPIO
import time
import spidev
from numpy import interp  # To scale values
from time import sleep  # To add delay


# Moisture sensor channel on MCP3008
moisture_channel = 0

GPIO.setmode(GPIO.BCM)

#hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


# GPIO.setup(18, GPIO.OUT)
GPIO.setup(moisture_channel, GPIO.IN)

# threshold = 10

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)

# Function to read SPI data from MCP3008 chip
def ReadChannel(channel):
    adc = spi.xfer2([1, (8+channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

# Function to read sensor connected to MCP3008
def readMoisture():
    level = ReadChannel(moisture_channel)
    return level

# Controller main function
def runController():
    level = readMoisture()

# Check moisture.format(level)
   if (level < 10.0):
       GPIO.output(26, True)
       sleep(0.5)
       print("Now it is watering")
   else:
       GPIO.output(26, False)

    

while True:
  level = ReadChannel(moisture_channel)
  level = interp(level, [0, 1023], [100, 0])
  #print("Moisture:", int(level))
  print("The Moisture is: {0:0.1f}".format(level))
  sleep(2)
