from gpiozero import CPUTemperature
from time import sleep, strftime, time

cpu = CPUTemperature()

def write_temp(temp):
	with open("cputemp", "a") as log:
		log.write("{0},{1}\n".format(starftime("%Y-%m-%d %H:%<:%S"),str(temp)))
		
while True:
	temp = cpu.temperature
	write_temp(temp)
	break