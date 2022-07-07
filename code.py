import board
import time
import digitalio
import busio
import oled
oled.init()

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT


led.value = True
time.sleep(2)
led.value = False
time.sleep(0.5)
    

zc05 = busio.UART(board.GP4, board.GP5, baudrate=9600, parity='N')

while True:
        led.value = True
        data=bytearray([0xFF, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79])
        zc05.write(data)
        receive=bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        zc05.readinto(receive)
        #receive = mhz19c.read(9)
        ch4=receive[2]*256+receive[3]
        oled.setMmessage('CH4: '+str(ch4)+" ppm")
        print('CH4: '+str(ch4)+' ppm')
        led.value = False
        time.sleep(2)
        