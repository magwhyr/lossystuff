# lossystuff

# Step 1: buy hardware
## Hardware
* Raspberry Pi 3	
  * https://www.adafruit.com/product/3055
* potentiometer
  * https://www.sparkfun.com/products/9940
* volume knob (make sure it goes to 11)
  * https://www.sparkfun.com/products/11951
* ~~toggle switch~~
  * https://www.sparkfun.com/products/9276#reviews
  * Using a switch button instead
* 2.8" PiTFT capacitive screen
  * https://www.adafruit.com/product/2423
* PowerBoost charger
  * https://www.adafruit.com/product/2465
* 5V 2.4A Switching Power Supply
  * https://www.adafruit.com/product/1995
* Lithium Ion Polymer Battery - 3.7v 2500mAh
  * https://www.adafruit.com/product/328
* ~~MCP3008	Adafruit~~
  * https://www.adafruit.com/product/856
  * Using the ADS1115 instead because the PiTFT uses both SPI ports so I2C is the only thing left to use for potentiometer
* Samsung EVO 32GB Class 10 Micro SDHC Card with Adapter (MB-MP32DA/AM)
  * https://www.amazon.com/Samsung-Class-Adapter-MB-MP32DA-AM/dp/B00IVPU786/ref=sr_1_2?s=pc&ie=UTF8&qid=1491579374&sr=1-2&keywords=micro+sd+card&refinements=p_n_feature_two_browse-bin%3A6518304011
* White LED Backlight Module - Medium 23mm x 75mm
  * https://www.adafruit.com/product/1622
* ~~Tactile Button switch (6mm)~~
  * https://www.adafruit.com/product/367
* USB A/MicroB
  * https://www.adafruit.com/product/898
* Audio extender
  * https://www.adafruit.com/product/3319
* ~~HDMI extender~~
  * https://www.amazon.com/gp/product/B001K38Z2G/
  * Not providing a port for HDMI after all. It doesn't work anyways with the PiTFT.
    * but, it does now when using the fbcp, but still not providing an HDMI port anyway.
* Mini Fan
  * https://www.adafruit.com/product/3368
* ADS1115 16-Bit ADC - 4 Channel with Programmable Gain Amplifier
  * https://www.adafruit.com/product/1085
* White LED Arcade Buttons
  * https://www.adafruit.com/product/3429
  * Four of them to provide different playbac options.
* Metal LED Blue On/Off Switch
  * https://www.adafruit.com/product/915
  * Switch for running the safe shutdown script.
* Metal LED Red On/Off Switch
  * https://www.adafruit.com/product/916
  * Power switch to turn on/off power from the PowerBoost


# Step 2: Install the OS on SD card
## OS Setup
* Follow the directions here to install Adafruit's modified Raspbian OS onto the SD card
  * https://learn.adafruit.com/adafruit-2-8-pitft-capacitive-touch/easy-install
* Follow these instructions for setting up WiFi on UVA network
  * http://scholarslab.org/makerspace/raspberry-pi-on-uva-wifi-network/
* Follow these instructions for configuring to use the PiTFT display
  * https://learn.adafruit.com/adafruit-2-8-pitft-capacitive-touch/overview

## OS Setup 2
* Begin with the PiTFT unplugged
* Follow instructions for installing the latest Raspbian OS.
  * https://www.raspberrypi.org/documentation/installation/
* Follow these instructions for setting up WiFi on UVA network
  * http://scholarslab.org/makerspace/raspberry-pi-on-uva-wifi-network/
* Follow instructions for installing fbcp
  * https://learn.adafruit.com/running-opengl-based-games-and-emulators-on-adafruit-pitft-displays/pitft-setup
  * For the options, select:
    1. Select Project: (option 4) Configure options manually
    2. Select display type: (option 3) PiTFT / PiTFT Plus 2.8" capacitive
    3. HDMI Rotation: (option 1) Normal
    4. TFT (MADCTL) rotation: (option 4) 270
  * Add this to the /boot/config.txt file to get the orientation for the touch to be correct.
    * `dtoverlay=pitft28-capacitive,rotate=270,touch-swapxy,touch-invy,speed=32000000,fps=20`
      * NOTE: you may need to have `touch-invx` instead of `touch-invy` if the mouse cursor is not behaving in the right direction.
    * http://www.0xf8.org/2016/01/complete-rotation-support-for-the-adafruit-pitft-2-8-capacitive-touchscreen-display/
    * http://www.runeaudio.com/forum/adafruit-pitft-2-8-capacitive-screen-with-buttons-solved-t3964.html
    * 
      ```
      # Enable audio (loads snd_bcm2835)
      dtparam=audio=on

      # PiTFT 2.8" settings
      dtoverlay=pitft28-capacitive,rotate=270,touch-swapxy,touch-invy,speed=32000000,fps=20
      display_rotate=0

      # Great resolution for just the PiTFT (too low for monitor)
      #hdmi_group=2
      #hdmi_mode=87
      # Great screen resolution for having the monitor attached
      hdmi_group=1
      hdmi_mode=34

      hdmi_cvt=320 240 60 1 0 0 0
      start_x=0
      ```
    * Change all occurances of hdmi_group to 2 and hdmi_mod to 87


### Using a monitor instead
To use a monitor instead of the PiTFT, you'll need to edit the `/boot/config.txt` file.
- Comment out the lines you add in from above, all of the lines that begin with "dtoverlay" and "display_rotate" and "hdmi_cvt"
- Make sure the monitor is plugged in via HDMI
- You can follow the steps here, under "Which values are valid for my monitor?", to determine which mode to use.
  - https://www.raspberrypi.org/documentation/configuration/config-txt/video.md
  - Edit the "hdmi_group" and "hdmi_mode" lines based on the results of the steps outlined above.
- Leave everything uncommented and both work at the same time.

# Step 3: Power

Power is improved with the PowerBoost. The PowerBoost connects to the Raspberry
Pi with a micro USB to USB A adapter (https://www.adafruit.com/product/898).
Power to the PowerBoost is provided by the Lithium Ion Polymer Battery - 3.7v
2500mAh (https://www.adafruit.com/product/328) or a wall adapter. An on/off
switch, also connected to the PowerBoost, cuts power to the PowerBoost and Pi.

* There are two switches to controll power on the Pi. One is a simple on/off
  switch that connects to the PowerBoost charger that cuts power to the
  Raspberry Pi. A button allows for safe shutdown of the Raspberry Pi.
* The PiTFT comes with four buttons on the side, one is wired to provide the
  safe shutdown. To free this button and use our own, follow this tutorial
  * Use this script. https://github.com/scruss/shutdown_button.git 
  * The button should be physically plugged into BCM/GPIO 27.
  * To run the shutdown script, the button must go from an unpressed to pressed state.
* To add the on/off switch to the PowerBoost, follow this tutorial
  * https://learn.adafruit.com/adafruit-powerboost-500-plus-charger/on-slash-off-switch
  * Basically, solder the two wire switch to the GND and EN holes
  * The switch (https://www.adafruit.com/product/916) has a built in LED, so wiring is as such: 
    * + to 5v on the PowerBoost, and - to the Gnd on PowerBoost. C1 (common) on switch to Gnd on PowerBoost. NO1 (Noncommon Open) on switch to En on PowerBoost.

* The Fan is also connected to the PowerBoost. The same Gnd and 5v as the switch so that the fan is on when the system is on and off when the system is off.


# Step 4: Volume Control (it goes to 11)
- Add this line to `/boot/config.txt` to remove hissing from the 3.5mm audio output
  - `audio_pwm_mode=2`
- Analog to digital conversion is handled with the ADS1115 16-Bit ADC - 4 Channel with Programmable Gain Amplifier (https://www.adafruit.com/product/1085) The amplifier sits between the Pi and a potentiometer (https://www.sparkfun.com/products/9940) with a volume knob (make sure it goes to 11) (https://www.sparkfun.com/products/11951).
  - The ADC is connected to the Raspberry Pi 3V and Ground, and SCL to SCL, and SDA to SDA.
  - The potentiometer is connected to the Raspberry Pi 3V and Ground, and the middle connection to A0 on the ADC.
- Get the Python libraries for connecting with ADC
  - https://github.com/adafruit/Adafruit_Python_ADS1x15
  -
    ```
    sudo apt-get install git build-essential python-dev
    cd ~
    git clone https://github.com/adafruit/Adafruit_Python_ADS1x15.git
    cd Adafruit_Python_ADS1x15
    sudo python setup.py install
    ```
- And the python library for controlling the volume
  - https://stackoverflow.com/questions/41592431/changing-volume-in-python-program-on-raspbery-pi
  -
  ```
  sudo apt-get install python-alsaaudio
  ```
- Make a file at ~/volume-control/volume-control.py to control the volume
  - 
    ```
      import time
      import alsaaudio
      import Adafruit_ADS1x15

      adc = Adafruit_ADS1x15.ADS1115()
      m = alsaaudio.Mixer('PCM')

      current_volume = m.getvolume()

      # Choose a gain of 1 for reading voltages from 0 to 4.09V.
      # Or pick a different gain to change the range of voltages that are read:
      #  - 2/3 = +/-6.144V
      #  -   1 = +/-4.096V
      #  -   2 = +/-2.048V
      #  -   4 = +/-1.024V
      #  -   8 = +/-0.512V
      #  -  16 = +/-0.256V
      # See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
      GAIN = 1

      def maprange(VOL, POT, v):
          (VOL1, VOL2), (POT1, POT2) = VOL, POT
          return  POT1 + ((v - VOL1) * (POT2 - POT1) / (VOL2 - VOL1))

      while True:
          value = adc.read_adc(0, gain=GAIN)
          volume = maprange((0,26354), (0,100), value)
          if volume < 0:
              volume = 0
          m.setvolume(volume)
    ```

- Add this line to `~/.config/lxsession/LXDE-pi/autostart` to have the python script run on startup.
  - `/usr/bin/python /home/pi/volume-control/volume-control.py`

# Step 5: Get Processing to run the script at boot
- Make sure the resolution on the PiTFT is max at 320x240.
- Add this line to `~/.config/lxsession/LXDE-pi/autostart`
  - `/home/pi/processing-3.3.6/processing-java --sketch=/home/pi/sketchbook/modernistPi --run`

# Step 6: Hardware Assembly
