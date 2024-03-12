"""
IRI - TP1 - Ex 3
By: Gonçalo Leão
"""
import os
os.environ["WEBOTS_HOME"] = "/usr/local/webots"

import math
import time
from controller import Robot
from controllers.utils import *



robot: Robot = Robot()


#move_forward2(robot, 0.1, 0.1)

start_time = time.time()

cmd_vel(robot, 0.1, 0)
while time.time() - start_time < 1:
    robot.step(64)

time.sleep(1)


cmd_vel(robot, 0, 180)


while robot.step(64) != -1:
    pass

# TODO
