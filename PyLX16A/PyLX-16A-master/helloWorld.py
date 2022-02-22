from lx16a import *
from math import sin, cos

# This is the port that the controller board is connected to
# This will be different for different computers
# On Windows, try the ports COM1, COM2, COM3, etc...
# On Raspbian, try each port in /dev/
LX16A.initialize("COM5")

# There should two servos connected, with IDs 1 and 2
servo5 = LX16A(5)
servo6 = LX16A(6)
servo3 = LX16A(3)
servo1 = LX16A(1)
servo4 = LX16A(4)
servo2 = LX16A(2)
t = 0
pos5 = servo5.getPhysicalPos()
pos6 = servo5.getPhysicalPos()
pos3 = servo3.getPhysicalPos()
pos1 = servo1.getPhysicalPos()
pos4 = servo4.getPhysicalPos()
pos2 = servo2.getPhysicalPos()
print(pos2)
while True:
	# Two sine waves out of phase
	# The servos can rotate between 0 and 240 degrees,
	# So we adjust the waves to be in that range
	#servo2.moveTimeWrite(sin(t) * 10 + pos2)
	#servo5.moveTimeWrite(sin(t) * 10 + pos5)
	#servo1.moveTimeWrite(sin(t) * 10 + pos1)
	#servo3.moveTimeWrite(sin(t) * 10 + pos3)
	servo4.moveTimeWrite(sin(t) * 10 + pos4)

	t += 0.005
