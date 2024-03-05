"""
IRI - TP1 - Ex 6
By: Gonçalo Leão
"""

from controller import Robot
from controllers.utils import cmd_vel
import math

robot: Robot = Robot()

angular_velocity = 4*math.pi
linear_velocity = 1

while linear_velocity > 0:
    print(linear_velocity)
    cmd_vel(robot, linear_velocity, angular_velocity)
    robot.step(64)
    linear_velocity = linear_velocity/1.1

cmd_vel(robot, linear_velocity, angular_velocity)

while robot.step(64) != -1:
    pass

