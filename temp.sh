#!/bin/bash
(
cpuTemp0=$(cat /sys/class/thermal/thermal_zone0/temp)
cpuTemp1=$(($cpuTemp0/1000))
cpuTemp2=$(($cpuTemp0/100))
cpuTempM=$(($cpuTemp2 % $cpuTemp1))
date
echo $cpuTemp1.$cpuTempM
echo $cpuTemp1.$cpuTempM *1.8+32 | bc
) &>> templog
