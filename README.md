# lossystuff

# Step 1: buy hardware
## Hardware
* Raspberry Pi 3	
  * https://www.adafruit.com/product/3055
* potentiometer
  * https://www.sparkfun.com/products/9940
* volume knob
  * https://www.sparkfun.com/products/11951
* toggle switch
  * https://www.sparkfun.com/products/9276#reviews
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
* Tactile Button switch (6mm)
  * https://www.adafruit.com/product/367
* USB A/MicroB
  * https://www.adafruit.com/product/898
* Audio extender
  * https://www.adafruit.com/product/3319
* HDMI extender
  * https://www.amazon.com/gp/product/B001K38Z2G/
* Mini Fan
  * https://www.adafruit.com/product/3368
* ADS1115 16-Bit ADC - 4 Channel with Programmable Gain Amplifier
  * https://www.adafruit.com/product/1085

# Step 2: Install the OS on SD card
## OS Setup
* Follow the directions here to install Adafruit's modified Raspbian OS onto the SD card
  * https://learn.adafruit.com/adafruit-2-8-pitft-capacitive-touch/easy-install
* Follow these instructions for setting up WiFi on UVA network
  * http://scholarslab.org/makerspace/raspberry-pi-on-uva-wifi-network/
* Follow these instructions for configuring to use the PiTFT display
  * https://learn.adafruit.com/adafruit-2-8-pitft-capacitive-touch/overview

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
  * https://learn.adafruit.com/adafruit-pitft-28-inch-resistive-touchscreen-display-raspberry-pi/extras#tactile-switch-as-power-button
  * Basically, open the file at `/etc/modprobe.d/adafruit.conf` and edit the
    line in there. Change the `gpio_pin` to the desired GPIO pin. It should
    look like this: 
    * `options rpi_power_switch gpio_pin=23 mode=0`
* To add the on/off switch to the PowerBoost, follow this tutorial
  * https://learn.adafruit.com/adafruit-powerboost-500-plus-charger/on-slash-off-switch
  * Basically, solder the two wire switch to the GND and EN holes

