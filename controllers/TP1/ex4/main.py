"""
IRI - TP1 - Ex 4
By: Gonçalo Leão
"""

from controller import Robot
from controllers.utils import *
import time


robot: Robot = Robot()



# TODO

while True:
    move_forward(robot, 25 / 100, 0.1)
    time.sleep(1)
    move_forward(robot, 25 / 100, -0.1)
    time.sleep(1)

