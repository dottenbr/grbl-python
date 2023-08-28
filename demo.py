#!/usr/bin/env python

import serial
import time

# Open grbl serial port
s = serial.Serial('/dev/tty.usbserial-AQ02Z8ND', 11520) # put your serial port here
print('Connected to: ' + s.name)
print('Serial port open: ' + str(s.is_open))

# Serial write and readline
def send_gcode(gcode):
    s.write(str.encode(gcode))
    print('Sending: ' + str(str.encode(gcode)))
    print(s.readline().strip().decode('utf-8'))

# Wake up grbl
send_gcode('\r\n\r\n')
time.sleep(2)   # Wait for grbl to initialize
s.flushInput()  # Flush startup text in serial input
send_gcode('$X') # Reset errors
send_gcode('$H') # Homing
send_gcode('G1 X100 Y100 Z0.0 F5000') # Go to X:100, Y:100, Z:0.0 at 5000 mm/min

# Close serial port
s.close()
