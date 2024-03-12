"""
IRI - TP1 - Ex 1
By: Gonçalo Leão
"""
import os
os.environ["WEBOTS_HOME"] = "/usr/local/webots"


from controller import Robot
from controllers.utils import cmd_vel

timestep = 64

# Create the Robot instance.
robot: Robot = Robot()


# TODO: Use cmd_vel and robot.step()
cmd_vel(robot, 0.1, 0)


while robot.step(timestep) != -1:

    pass