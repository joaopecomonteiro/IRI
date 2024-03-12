"""
IRI - TP2 - Ex 1
By: Gonçalo Leão
"""

from controller import Robot, TouchSensor
from controllers.utils import *
import time

# Create the Robot instance.
robot: Robot = Robot()

timestep: int = int(robot.getBasicTimeStep())  # in ms

touch_sensor: TouchSensor = robot.getDevice('touch sensor')

touch_sensor.enable(timestep)

while True:
    cmd_vel(robot, 0.1, 0)

    if touch_sensor.getValue() == 1.0:

        start_time = time.time()
        while time.time() - start_time < 1:
            cmd_vel(robot, -0.1, 0)
            robot.step()

        start_time = time.time()
        while time.time() - start_time < 1:
            cmd_vel(robot, 0, math.pi/3)
            robot.step()

    cmd_vel(robot, 0.1, 0)

    robot.step()






