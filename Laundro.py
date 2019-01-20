import requests
import datetime
import math
import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import json

MACHINE_COUNT = 1
MACHINE_THRESHOLD = [3.0] * MACHINE_COUNT
machine_status = [False] * MACHINE_COUNT
# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
chan = []
chan.append( AnalogIn(ads, ADS.P0) )

# Create differential input between channel 0 and 1
#chan = AnalogIn(ads, ADS.P0, ADS.P1)

#machines = list(MACHINE_COUNT)

# print("{:>5}\t{:>5}".format('raw', 'v'))
def available(): #boolean
    ave_val = monitor_average() #ave volt over 10s
    should_update_server = True # change later
    for j in range(MACHINE_COUNT):
        new_status = ave_val[j] > MACHINE_THRESHOLD[j] 
        if new_status != machine_status[j]:
            should_update_server = True
            machine_status[j] = new_status      

    if should_update_server:
        out = {}
        for j in range(MACHINE_COUNT):
            out['hello'+str(j)] = {'minsleft':'god knows', 'available':machine_status[j],'intensity':ave_val[j]}

        out_json = json.dumps(out)
        with open('data.json', 'w') as outfile:
            json.dump(out_json, outfile)
        print(out_json) #will be pushed
    else:
        print('static')
    print('end of monitoring')
def createDict():
    ndict = {}
    for j in range(MACHINE_COUNT):
        ndict['hello'+str(j)] = {'minsleft':'god knows', 'available':machine_status[j]}
    return ndict

def monitor_average():
    lst = [0.0]*MACHINE_COUNT
    for i in range(20):
        for j in range(MACHINE_COUNT):  
            # chan.value
            lst[j] = lst[j] + (chan[j].voltage) * 0.1
            time.sleep(0.5/MACHINE_COUNT)
    return lst   

while True:
    valueToBePushed = available()
    

