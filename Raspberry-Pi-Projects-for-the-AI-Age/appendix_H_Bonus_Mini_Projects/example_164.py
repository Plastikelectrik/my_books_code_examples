from gpiozero import PWMOutputDevice, CPUTemperature
from time import sleep

fan = PWMOutputDevice(18, frequency=25)   # GPIO18
cpu = CPUTemperature()
while True:
    duty = fan_speed(cpu.temperature, fan.value > 0)
    fan.value = duty
    sleep(5)
