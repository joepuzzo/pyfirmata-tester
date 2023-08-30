from pyfirmata import Arduino, util
import time

# Initialize the board
# Replace '/dev/ttyUSB0' with the appropriate port for your system
board = Arduino('/dev/tty.usbmodem21401')

# Define a pin object for digital pin 13
# 'd' for digital, 13 for pin number, 'o' for output
led_pin = board.get_pin('d:13:o')

# Blink the LED
while True:
    led_pin.write(1)  # Turn LED on
    time.sleep(1)  # Wait for 1 second
    led_pin.write(0)  # Turn LED off
    time.sleep(1)  # Wait for 1 second
