# Simple demo of continuous ADC conversion mode for channel 0 of the ADS1x15 ADC.
# Author: Tony DiCola
# License: Public Domain
import time
import os

# Import the ADS1x15 module.
import Adafruit_ADS1x15

DEBUG = 1

# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()

# Scale Gain to +/- 5V from 4.096 V Default
GAIN = 0.8192

# Start continuous ADC conversions on channel 0 using the previously set gain
# value.  Note you can also pass an optional data_rate parameter, see the simpletest.py
# example and read_adc function for more infromation.
adc.start_adc(0, gain=GAIN)



potentiometer_adc = 0;
 
last_read = 0       # this keeps track of the last potentiometer value
tolerance = 5       # to keep from being jittery we'll only change
                    # volume when the pot has moved more than 5 'counts'
 
while True:
        # we'll assume that the pot didn't move
        trim_pot_changed = False
 
        # read the analog pin
        trim_pot = adc.get_last_result()
        # how much has it changed since the last read?
        pot_adjust = abs(trim_pot - last_read)
 
        if DEBUG:
                print "trim_pot:", trim_pot
                print "pot_adjust:", pot_adjust
                print "last_read", last_read
 
        if ( pot_adjust > tolerance ):
               trim_pot_changed = True
 
        if DEBUG:
                print "trim_pot_changed", trim_pot_changed
 
        if ( trim_pot_changed ):
                set_volume = trim_pot / 327.68           # convert 16bit adc0 (0-32768) trim pot read into 0-100 volume level
                set_volume = round(set_volume)          # round out decimal value
                set_volume = int(set_volume)            # cast volume as integer
 
                print 'Volume = {volume}%' .format(volume = set_volume)
                set_vol_cmd = 'sudo amixer cset numid=1 -- {volume}% > /dev/null' .format(volume = set_volume)
                os.system(set_vol_cmd)  # set volume
 
                if DEBUG:
                        print "set_volume", set_volume
                        print "tri_pot_changed", set_volume
 
                # save the potentiometer reading for the next loop
                last_read = trim_pot
 
        # hang out and do nothing for a half second
        time.sleep(0.5)
