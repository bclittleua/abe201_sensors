#ABE201 Environmental Sensor Suite v1.1
#bclittle@email.arizona.edu
#this code requires several dependencies:
#https://github.com/bclittleua?tab=repositories for more info

import datetime
import time
import RPi.GPIO as GPIO, time, os
import Adafruit_DHT
import Adafruit_ADS1x15

DEBUG = 1
GPIO.setmode(GPIO.BCM)

def RCtime (RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(0.1)

        GPIO.setup(RCpin, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(RCpin) == GPIO.LOW):
                reading += 1
        return reading

now = datetime.datetime.now()

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1

# set delay in seconds, 900 = 15 minutes
delay = 900

#setup for humidity sensor
sensor = Adafruit_DHT.DHT11
pin = 4
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
temperatureF = temperature * 1.8 + 32

while True:
        print "____________________________________"
        print str(now)
        tgs = [0]*4
        for i in range(4):
                tgs[i] = round((adc.read_adc(i, gain=GAIN) / 3.3 * .100), 2)
        print("Air Contaminants : {3} ppm". format(*tgs))
        ldr = round((RCtime(18)), 2)
        print("Light Intensity :{} (less is more!)". format(ldr))

        if temperature is not None:
                print('Temperature : {0:0.1f} *C'.format(temperature))
                print('Temperature : {0:0.1f} *F'.format(temperatureF))
        else:
                print('Temperature read failed.')

        if humidity is not None:
                print('Humidity : {0:0.1f} %'.format(humidity))
        else:
                print('Humidity read failed.')

#trying to append all that to a log
        slog = open('sensorlog', 'a+')
        slog.write('{},'.format(now))
        slog.write('{3},'.format(*tgs))
        slog.write('{},'.format(ldr))
        slog.write('{0:0.1f},'.format(temperature))
        slog.write('{0:0.1f},'.format(temperatureF))
        slog.write('{0:0.1f}\n'.format(humidity))
        slog.close()

        #time.sleep(delay)
	break
