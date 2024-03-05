"""
IRI - TP2 - Ex 2
By: Gonçalo Leão
"""
import math
from controller import Robot, DistanceSensor
from controllers.utils import cmd_vel

# Create the Robot instance.
robot: Robot = Robot()

timestep: int = int(robot.getBasicTimeStep())  # in ms


ps6: DistanceSensor = robot.getDevice('ps6')
ps6.enable(timestep)

ps7: DistanceSensor = robot.getDevice('ps7')
ps7.enable(timestep)

ps0: DistanceSensor = robot.getDevice('ps0')
ps0.enable(timestep)

ps1: DistanceSensor = robot.getDevice('ps1')
ps1.enable(timestep)
cmd_vel(robot, 0.1, 0)

while True:
    v6, v7, v0, v1 = ps6.getValue(), ps7.getValue(), ps0.getValue(), ps1.getValue()

    #print(v7, v0)

    if v6 > 100 or v7 > 100 or v0 > 100 or v1 > 100:
        cmd_vel(robot, 0, math.pi/2)
        print()
        while v6 > 100 or v7 > 100 or v0 > 100 or v1 > 100:
            v6, v7, v0, v1 = ps6.getValue(), ps7.getValue(), ps0.getValue(), ps1.getValue()
            #print(v7, v0)
            robot.step()
    cmd_vel(robot, 0.1, 0)
    robot.step()


