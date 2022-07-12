# Mobile-Methane-Detector
It can measure methane gas up to 1.25% concentration (25%LEL) with a resolution of 100 ppm.
![IMG_4137](https://user-images.githubusercontent.com/108894502/177846188-3d656a36-0b18-4d55-acd3-c45e23871730.jpeg)

# Hardware
1. [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/) as microcontroller

2. [Winsen ZC05](https://www.winsen-sensor.com/sensors/combustible-sensor/zc05.html) as methane sensor (UART)

3. 0.91 Inch 128 × 32 IIC I2C OLED LCD Display

4.  5V, 2.4A mobile battery or 4 AA batteries (6V)

# Connection diagram

https://github.com/satoshi-nakao28/Mobile-Methane-Detector/issues/4#issue-1301387036

# Programming Language

[Adafruit CircuitPython for Raspberry Pi Pico](https://circuitpython.org/board/raspberry_pi_pico/) v7

# Attention

Operation with mobile batteries and dry cell batteries may be unstable. The cause is unknown, but I believe it is due to a power supply-related problem.
