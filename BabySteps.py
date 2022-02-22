#Baby steps
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

# This is the port that the controller board is connected to
# This will be different for different computers
# On Windows, try the ports COM1, COM2, COM3, etc...
# On Raspbian, try each port in /dev/
LX16A.initialize("/dev/ttyUSB0")

# There should two servos connected, with IDs 1 and 2
servo5 = LX16A(5)
pos5 = servo5.getPhysicalPos()
servo3 = LX16A(3)
pos3 = servo3.getPhysicalPos()
servo6 = LX16A(6)
pos6 = servo6.getPhysicalPos()
servo1 = LX16A(1)
pos1 = servo1.getPhysicalPos()
servo2 = LX16A(2)
pos2 = servo2.getPhysicalPos()
servo4 = LX16A(4)
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

    servo5.moveTimeWrite(sin(t) * 3.5 +  pos5)
	servo3.moveTimeWrite(sin(t) * 5.7 +  pos3)
	servo6.moveTimeWrite(sin(t) * 4.02 +  pos6)
	servo1.moveTimeWrite(cos(t) * 3.55 +  pos1)
	servo4.moveTimeWrite(-cos(t) * 5.75 +  pos4)
    servo2.moveTimeWrite(cos(t) * 4.00 +  pos2)
	t += 0.08