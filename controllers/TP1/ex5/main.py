"""
IRI - TP1 - Ex 5
By: Gonçalo Leão
"""

import math
from controller import Robot
from controllers.utils import move_forward, rotate
import time

robot: Robot = Robot()
while True:
    move_forward(robot, 25/100, 0.1)

    start_time = time.time()

    rotate(robot, math.pi/2, math.pi/2)

# TODO


