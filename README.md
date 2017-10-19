# abe201_sensors
This folder contains python code for ABE201 compost experiment.

Sensor Package Requires:
-  Raspberry Pi 3
-  breadboard (x2)
-  Adafruit ADS1115 Analog to Digital Converter (requires Adafruit_Python_ADS1x15 library)
-  TGS-2600 General Air Quality Sensor
-  DHT11 Temp/Humidity Sensor (requires Adafruit_Python_DHT library)
-  Light Detecting Resistor (LDR)
-  10k resistor
-  1uf >=5v Capacitor(1 microfarad greater-than or equal-to 5 volts DC)
-  Jumper Wires (aprox. 12)

See ABE201_group_lab.PDF for detailed instructions, but note that steps to import ADS/DHT libraries are not included, see below.


##INSTRUCTIONS FOR CIRCUIT ASSEMBLY:

###Wiring: ADC to Cobbler
Datasheet: https://cdn-shop.adafruit.com/datasheets/ads1115.pdf 

The RPi is not capable of reading analog values. The ADC module reads the analog signal and converts into a digital value the RPi can read. 
•	VDD - 3.3v pin 1 
•	GND - GND (any) 
•	SCL - SCL pin 5 
•	SDA - SDA pin 3  
•	A0 - n/a
•	A1 - n/a
• A2 - n/a
•	A3 - TGS2600 A0

###WIRING: DHT11 
Datasheet: http://www.micropik.com/PDF/dht11.pdf 

Measures temperature and humidity with a fair amount of accuracy (the DHT22 is more accurate, and other models include additional environmental sensors, such as barometric pressure). 
•	VCC - 3v3 (either pin 1 of cobbler or VCC of ADC), bridge to DATA w/ 10k resistor 
•	DATA - pin 7 (GPIO 4) cobbler, bridge to VCC w/ 10k resistor 
•	GND -  GND (any)
 
###WIRING: TGS2600 
Datasheet: http://www.figarosensor.com/products/2600pdf.pdf 

Detects Carbon Monoxide, Hydrogen, Methane (CH4), Ethanol, and Iso-butane by measuring electrical conductivity across a built-in heating element. It only spits out one number, which can be interpreted as parts per million. Review datasheet for more details. 
•	G - GND (any) 
•	AO - a3 of ADC 
•	DO - not used 
•	V - 5v, pin 2 or 4 of cobbler

###WIRING: LDR (bipolar, pick a leg) 
Datasheet: http://kennarar.vma.is/thor/v2011/vgr402/ldr.pdf 

This sensor works by reading the voltage built up in the capacitor rather than by measuring resistance directly. 
•	pin 1 - 3.3v 
•	pin 2 - pin 12 (GPIO 18) of cobbler w/ a 1uf >=5v capacitor tied to GND (capacitor is NOT bipolar, + to pin 12(GPIO 18) and - to GND)
