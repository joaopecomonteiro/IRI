"""
IRI - TP1 - Ex 2
By: Gonçalo Leão
"""

from controller import Robot
from controllers.utils import cmd_vel

robot: Robot = Robot()

# TODO

v = 0.1
r = 12.5 / 100
w = v/r
print(w)
cmd_vel(robot, v, w)


while robot.step(64) != -1:
    pass