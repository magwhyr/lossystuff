#!/usr/bin/python
 
# Source: https://www.raspberrypi.org/forums/viewtopic.php?f=9&t=5583


import spidev
import time
import os
import math
from mpd import MPDClient

# Get Static Sound from MPD playlist


# Connect to MPD server
client = MPDClient()
client.timeout = 5
client.connect("localhost",6600)
#print client.playlistsearch("any","RadioTune.mp3")
for song in client.playlistsearch("any","RadioTune.mp3"): # Change this to the name of the audio 
  song_id = song["id"]					#file you want to play from MPD playlist
  song_time = song["time"]
  song_time = int(song_time) + 5

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
 
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
 
# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def ConvertVolts(data,places):
  volts = (data * 3.3) / float(1023)
  volts = round(volts,places)
  return volts
 
# Define sensor channels
vol_channel = 0
tune_channel = 1
#etc
 
# Define delay between readings
vol_delay = .5
tune_delay = 5
step = 0

# Define tolernances
vol_last_read = 0
tune_last_read = 0
vol_tolerance = 10
tune_tolerance = 5

while True:

  trim_pot_changed = False
  tune_pot_changed = False
 
  # Read the pot data
  vol_level = ReadChannel(vol_channel)
  vol_volts = ConvertVolts(vol_level,2)
  tune_level = ReadChannel(tune_channel)
  tune_volts = ConvertVolts(tune_level,2)

  tune_actual = (math.log(tune_level + 1,10) * 341) / 10.24
  tune_actual = round(tune_actual)
  tune_actual = int(tune_actual)

  vol_pot_adjust = abs(vol_level - vol_last_read)
  tune_pot_adjust = abs(tune_actual - tune_last_read)

  if ( vol_pot_adjust > vol_tolerance ):
    trim_pot_changed = True
  if ( tune_pot_adjust > tune_tolerance ):
    tune_pot_changed = True

  if ( trim_pot_changed ):
    # convert 10bit adc0 (0-1024) trim pot read into 0-100 volume level with LOG correction
    set_volume = (math.log(vol_level + 1,10) * 341) / 10.24
    set_volume = round(set_volume)          # round out decimal value
    set_volume = int(set_volume)            # cast volume as integer
 
    set_vol_cmd = 'sudo amixer cset numid=1 -- {volume}% > /dev/null' .format(volume = set_volume)
    os.system(set_vol_cmd)  # set volume
 
    # Print out results
    print "--------------------------------------------"
    print("Volts : {} ({}V)".format(vol_level,vol_volts))
    print "Volume: ", set_volume

    vol_last_read = vol_level

  if ( tune_pot_changed ): #is True and step >= tune_delay):

    # Print out results
    print "--------------------------------------------"
    print "Tuner Change Detected"

    # Play the tuner change sound
    client.playid(song_id)
    print "Start"
    time.sleep(song_time)
    print "Stop"
    tune_level = ReadChannel(tune_channel)
    tune_actual = (math.log(tune_level + 1,10) * 341) / 10.24
    tune_actual = round(tune_actual)
    tune_actual = int(tune_actual)
    tune_last_read = tune_actual

#    step = 0
#  else:
#    step = step + vol_delay

  # Wait before repeating loop

  time.sleep(vol_delay)
