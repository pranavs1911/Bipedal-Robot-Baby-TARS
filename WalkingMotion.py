"""
WalkingMotion.py
Author: Pranav Shankar.S (spranav1911@gmail.com)
Lewansoul library: Ethan Lipson
"""
#3 is right feet
#5 is right thigh
#6 is right calf
#1 is left thigh
#2 is left calf
#4 is left feet
#initial - 1 - 198
#initial - 2 - 138
#initial - 3 - 76
#initial - 4 - 111
#initial - 5 - 121
#initial - 6 - 59
from lx16a import *
from math import sin, cos
import time

# This is the port that the controller board is connected to
# This will be different for different computers
# On Windows, try the ports COM1, COM2, COM3, etc...
# On Raspbian, try each port in /dev/
LX16A.initialize("/dev/ttyUSB0")
servo1 = LX16A(1)
servo2 = LX16A(2)
servo3 = LX16A(3)
servo4 = LX16A(4)
servo5 = LX16A(5)
servo6 = LX16A(6)

# There should two servos connected, with IDs 1 and 2
def ProportionalControl(motor_angle, desired_angle):
	motor_angle = 1.12*(desired_angle - motor_angle) + motor_angle
	return motor_angle

def checkStability(value1, value2, value3, value4, value5, value6):
	global servo1, servo2, servo3
	global servo4, servo5, servo6

	#For condition 1
	if (abs(value5 - value6) >= 80):
		value6 = ProportionalControl(value6,(value6 - 25))
	if (abs(value1 - value2) <= 75):
		value2 = ProportionalControl(value2, (value2 + 25))

	# For condition 2
	if (abs(value3 - value6) >= 30):
		value3 = ProportionalControl(value3, (value3 - 7.5))
	if (abs(value2 - value4) <= 30):
		value4 = ProportionalControl(value4, (value4 + 7.5))
	servo2.moveTimeWrite(value2)
	servo3.moveTimeWrite(value3)
	servo4.moveTimeWrite(value4)
	servo6.moveTimeWrite(value6)
def run():
	global servo1, servo2, servo3
	global servo4, servo5, servo6
	pos5 = servo5.getPhysicalPos()
	pos3 = servo3.getPhysicalPos()
	pos6 = servo6.getPhysicalPos()

	pos1 = servo1.getPhysicalPos()
	pos2 = servo2.getPhysicalPos()
	pos4 = servo4.getPhysicalPos()
	print(pos1)
	print(pos2)
	print(pos3)
	print(pos4)
	print(pos5)
	print(pos6)
	t = 0
	servo1.moveTimeWrite(40)
	servo2.moveTimeWrite(31)
	servo3.moveTimeWrite(29)
	servo4.moveTimeWrite(71)
	servo5.moveTimeWrite(5)
	servo6.moveTimeWrite(164)
	while True:
		# Two sine waves out of phase
		# The servos can rotate between 0 and 240 degrees,
		# So we adjust the waves to be in that range
		value5 = sin(t) * 3.5 + pos5
		servo5.moveTimeWrite(sin(t) * 3.5 + pos5)
		servo5.moveTimeWrite(ProportionalControl(servo5.getPhysicalPos(),value5))
		time.sleep(0.005)

		value3 = sin(t) * 5.7 + pos3
		servo3.moveTimeWrite(sin(t) * 5.7 + pos3)
		servo3.moveTimeWrite(ProportionalControl(servo3.getPhysicalPos(),value3))
		time.sleep(0.005)

		value6 = sin(t) * 4.02 + pos6
		servo6.moveTimeWrite(sin(t) * 4.02 + pos6)
		servo6.moveTimeWrite(ProportionalControl(servo6.getPhysicalPos(),value6))
		time.sleep(0.005)

		value1 = cos(t) * 3.55 + pos1
		servo1.moveTimeWrite(cos(t) * 3.55 + pos1)
		servo1.moveTimeWrite(ProportionalControl(servo1.getPhysicalPos(),value1))
		time.sleep(0.005)

		value4 = -cos(t) * 5.75 + pos4
		servo4.moveTimeWrite(-cos(t) * 5.75 + pos4)
		servo4.moveTimeWrite(ProportionalControl(servo4.getPhysicalPos(), value4))
		time.sleep(0.005)

		value2 = cos(t) * 4.00 + pos2
		servo2.moveTimeWrite(cos(t) * 4.00 + pos2)
		servo2.moveTimeWrite(ProportionalControl(servo2.getPhysicalPos(),value2))
		time.sleep(0.005)
		checkStability(servo1.getPhysicalPos(), servo2.getPhysicalPos(), servo3.getPhysicalPos(), servo4.getPhysicalPos(), servo5.getPhysicalPos(), servo6.getPhysicalPos())

		t += 0.08

if __name__ == "__main__":
	run()