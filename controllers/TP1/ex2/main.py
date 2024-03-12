"""
IRI - TP1 - Ex 2
By: Gonçalo Leão
"""
import os
os.environ["WEBOTS_HOME"] = "/usr/local/webots"

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