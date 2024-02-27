"""
IRI - TP1 - Ex 6
By: Gonçalo Leão
"""

from controller import Robot
from controllers.utils import cmd_vel
import math

robot: Robot = Robot()

radius = 2*math.pi
linear_velocity = 0.5

while True:

    cmd_vel(robot, linear_velocity, radius)
    robot.step(64)
    linear_velocity -= 0.01
# TODO

