#!/usr/bin/python



import time

import Image
import ImageDraw

from Adafruit_LED_Backpack import Matrix8x8



# Create display instance on default I2C address (0x70) and bus number.
display = Matrix8x8.Matrix8x8()

# Alternatively, create a display with a specific I2C address and/or bus.
# display = Matrix8x8.Matrix8x8(address=0x74, busnum=1)

# Initialize the display. Must be called once before using the display.
display.begin()


heart1=[0b00000000, 0b01100110, 0b10011001, 0b10000001, 0b01000010, 0b00100100, 0b00011000, 0b00000000]

heart2=[0b00000000, 0b01100110, 0b11111111, 0b11111111, 0b01111110, 0b00111100, 0b00011000, 0b00000000]



while(True):



  for y in range(0, 8):

    position = 128

    for x in range(0, 8):

      value = position & heart1[y]

      if (value > 0):

        value = red

      display.set_pixel(x, y, value )

      position = position >> 1



  time.sleep(0.5)



  for y in range(0, 8):

    position = 128

    for x in range(0, 8):

      value = position & heart2[y]

      if (value > 0):

        value = red

      display.set_pixel(x, y, value )

      position = position >> 1



  time.sleep(1)