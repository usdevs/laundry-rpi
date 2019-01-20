import requests
import datetime
import math
import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)

# Create differential input between channel 0 and 1
#chan = AnalogIn(ads, ADS.P0, ADS.P1)

# print("{:>5}\t{:>5}".format('raw', 'v'))
def available(x): #boolean
    ave_val = monitor_average() #ave volt over 10s
    if ave_val > x:
        return True
    return False


def monitor_average():
    lst = []
    for i in range(5):
        # chan.value
        lst.append(chan.voltage)
        time.sleep(0.5)
    return sum(lst)/len(lst)

try:
    while True:
        valueToBePushed = available(3)
        print('00ga b00ga')
except KeyboardInterrupt:
    print("No stopping!!!")
    valueToBePushed = available(3)
    print('willy wonka')
