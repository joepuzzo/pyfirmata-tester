from pyfirmata import Arduino, util
import time

# Initialize the board
# Replace '/dev/ttyUSB0' with the appropriate port for your system
board = Arduino('/dev/tty.usbmodem21301')

# Start an iterator thread so that the serial buffer doesn't overflow
it = util.Iterator(board)
it.start()

# Define a pin object for analog pin A0 and digital pin 9
# 'a' for analog, 0 for pin number, 'i' for input
fsr_pin = board.get_pin('a:0:i')
# 'd' for digital, 9 for pin number, 'p' for PWM output
led_pin = board.get_pin('d:9:p')

# Allow some time for the iterator to read initial values
time.sleep(1)

# Read from the FSR sensor and control LED brightness
while True:
    fsr_reading = fsr_pin.read()
    if fsr_reading is not None:
        # Ensure the scaled_value is within 0-255
        scaled_value = min(max(int(fsr_reading * 255), 0), 255)
        # pyFirmata expects a value between 0 and 1 for PWM
        led_pin.write(scaled_value / 255.0)
        print(f"FSR reading: {fsr_reading}, Scaled value: {scaled_value}")
    time.sleep(0.04)  # Approximately 25 Hz (1/0.04 = 25)
