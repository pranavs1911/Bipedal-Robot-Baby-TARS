#joint0 is right thigh
#joint1 is right calf
#joint2 is right feet
#joint3 is left thigh
#joint4 is left calf
#joint5 is left feet

import pybullet as p
import time
import pybullet_data
import math
import matplotlib.pyplot as m
import numpy as np
physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setPhysicsEngineParameter(enableFileCaching=0)
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
p.setGravity(0,0,-10)
planeId = p.loadURDF("plane.urdf")
cubeStartPos = [0,0,0.40]
useFixedBase = 1
cubeStartOrientation = p.getQuaternionFromEuler([1.65,0,1.75])
boxId = p.loadURDF("tries.urdf",cubeStartPos, cubeStartOrientation,useFixedBase)
#print(p.getLinkState(boxId, linkIndex = 0))

#Sets the joint states of the robot
joint0 = p.getJointState(boxId, jointIndex = 0)
joint1 = p.getJointState(boxId, jointIndex = 1)
joint2 = p.getJointState(boxId, jointIndex = 2)
joint3 = p.getJointState(boxId, jointIndex = 3)
joint4 = p.getJointState(boxId, jointIndex = 4)
joint5 = p.getJointState(boxId, jointIndex = 5)
maxForce = 500
mode = p.POSITION_CONTROL

#Sets the initial joint motor angle
p.setJointMotorControl2(boxId, jointIndex=0, controlMode=mode, targetPosition = joint0[0])
p.setJointMotorControl2(boxId, jointIndex=3, controlMode=mode, targetPosition = joint3[0])
p.setJointMotorControl2(boxId, jointIndex=1, controlMode=mode, targetPosition = joint1[0])
p.setJointMotorControl2(boxId, jointIndex=2, controlMode=mode, targetPosition = joint2[0])
p.setJointMotorControl2(boxId, jointIndex=4, controlMode=mode, targetPosition = joint4[0])
p.setJointMotorControl2(boxId, jointIndex=5, controlMode=mode, targetPosition = joint5[0])

#jointIndex1 = 0
#jointIndex2 = 3
#jointIndex3 = 3
m.xlabel('Time')
m.ylabel('Joint Position')
joint0dup = []
joint1dup = []
joint2dup = []
joint3dup = []
joint4dup = []
idup = []
print(math.cos(3.14))

#Runs the Simulation for 10 secs
for i in range (10000):
    joint0 = p.getJointState(boxId, jointIndex=0)
    joint1 = p.getJointState(boxId, jointIndex=1)
    joint2 = p.getJointState(boxId, jointIndex=2)
    joint3 = p.getJointState(boxId, jointIndex=3)
    joint4 = p.getJointState(boxId, jointIndex=4)
    joint5 = p.getJointState(boxId, jointIndex=5)

    #Sets the joint motor control for the robot
    p.setJointMotorControl2(boxId, jointIndex=0, controlMode=mode, targetPosition=joint0[0] + 0.1*math.sin(0.09*i))
    p.setJointMotorControl2(boxId, jointIndex=3, controlMode=mode, targetPosition=joint3[0] + 0.1*math.cos(0.09*i))
    p.setJointMotorControl2(boxId, jointIndex=1, controlMode=mode, targetPosition=joint1[0] + 0.13*math.sin(0.07*i))
    p.setJointMotorControl2(boxId, jointIndex=2, controlMode=mode, targetPosition=joint2[0] + 0.11*math.sin(0.04*i))
    p.setJointMotorControl2(boxId, jointIndex=4, controlMode=mode, targetPosition=joint4[0] + 0.13*math.cos(0.07*i))
    p.setJointMotorControl2(boxId, jointIndex=5, controlMode=mode, targetPosition=0.11*math.sin(0.04*i))
    m.show()
    p.setJointMotorControl2(boxId, jointIndex3, controlMode=mode, targetPosition=0.4)

    #Acquires the joint motor angle
    joint0dup.append(p.getJointState(boxId, jointIndex = 0)[0])
    joint1dup.append(p.getJointState(boxId, jointIndex = 1)[0])
    joint2dup.append(p.getJointState(boxId,jointIndex = 2)[0])
    joint3dup.append(p.getJointState(boxId, jointIndex=3)[0])
    joint4dup.append(p.getJointState(boxId, jointIndex=4)[0])

    #Simulates Forward Kinematics

    #Forward Kinematics
    #joint0r = joint0[0]*3.14/180
    #joint1r = joint1[0]*3.14/180
    #joint2r = joint2[0]*3.14/180
    #Rot1 = np.array(([1,0,0,0],[0,np.cos(joint0r), -np.sin(joint0r),0],[0,np.sin(joint0r),np.cos(joint0r), 0],[0,0,0,1]))
    #Rot2 = np.array(([1, 0, 0,0], [0, np.cos(joint1r), -np.sin(joint1r), 0],[0, np.sin(joint1r), np.cos(joint1r),0],[0,0,0,1]))
    #Rot3 = np.array(([1,0,0,0],[0,np.cos(joint2r), -np.sin(joint2r), 0],[0,np.sin(joint2r), np.cos(joint2r), 0],[0,0,0,1]))
    #Trans1 =  np.array(([1,0,0,0],[0,1,0,0.06454],[0,0,1, 0.03033],[0,0,0,1]))
    #Trans2 = np.array(([1,0,0,0],[0,1,0,0.01119], [0,0,1,0.10702], [0,0, 0,1]))
    #Trans3 = np.array(([1,0,0,0],[0,1, 0, 0.01876], [0,0, 1, 0.03631], [0,0, 0, 1]))
    #TransB = np.array(([1,0,0,0],[0,1, 0, 0.04], [0,0, 1, 0.1237], [0,0, 0, 1]))

    #print("Joint1\n", joint0r)
    #print("Joint0\n", joint1r)
    #print("Joint2\n", joint2r)
    #Fkin = TransB*Rot1*Trans1*Rot2*Trans2*Rot3*Trans3
    #Forward Kinematics Equation is Rot1*Trans1*Rot2*Trans2*Rot3*Trans3
    #idup.append(i)
    #m.ylim(2.54e-313, 2.55e-313)
    #m.plot(i, p.getJointState(boxId, jointIndex=2)[0])
    #m.show()
    p.stepSimulation()
    time.sleep(1./1480.)

#Acquires cube orientation at the end of the simulation
cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
print(cubePos,cubeOrn)
p.disconnect()
