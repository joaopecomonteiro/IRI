"""
IRI - TP2 - Ex 3
By: Gonçalo Leão
"""

import math

from controller import Robot, GPS, Compass
from controllers.utils import cmd_vel

# Create the Robot instance.
robot: Robot = Robot()

timestep: int = int(robot.getBasicTimeStep())


compass: Compass = robot.getDevice('compass')
compass.enable(timestep)

gps: GPS = robot.getDevice('gps')
gps.enable(timestep)

cmd_vel(robot, 0, 0)
robot.step()

while True:
    init_gps_vals = gps.getValues()
    init_compass_vals = compass.getValues()

    cmd_vel(robot, 0.1, 0)
    gps_vals = gps.getValues()
    while 

    #cmd_vel(robot, 0.1, 0)
    #robot.step(1000)

    #cmd_vel(robot, 0, math.pi/2)
    #robot.step(1000)



    print(f"compass: {compass.getValues()}")
    print(f"gps: {gps.getValues()}")
    print("-------------------------------")