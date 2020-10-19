import RPi.GPIO as GPIO
import time
import spidev

# Moisture sensor channel on MCP3008
moisture_channel = 0

GPIO.setmode(GPIO.BCM)


GPIO.setup(18, GPIO.OUT)

threshold = 10

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
    if (level < threshold):
        GPIO.output(18, True)
    else:
        GPIO.output(18, False)

    print("Moisture: {0:0.1f}".format(level))

while True:
    runController()
    time.sleep(10)
