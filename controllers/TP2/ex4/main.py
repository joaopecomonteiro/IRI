"""
IRI - TP2 - Ex 4
By: Gonçalo Leão
"""

import os
os.environ["WEBOTS_HOME"] = "/usr/local/webots"

import pdb

import math

from numpy import random
import numpy as np

from controller import Robot, Lidar
from controllers.utils import cmd_vel

def distance_handler(direction: int, dist_values: [float]) -> (float, float):
    maxSpeed: float = 0.1
    distP: float = 10.0
    angleP: float = 7.0
    wallDist: float = 0.1

    # Find the angle of the ray that returned the minimum distance
    # TODO
    min_dist = np.inf
    min_idx = 0
    for idx, value in enumerate(dist_values):
        if value < min_dist:
            min_dist = value
            min_idx = idx

    #print(f"min_dist: {min_dist}")

    n_lasers = len(dist_values)
    inc = math.pi*2/(n_lasers-1)
    angle_min = inc*min_idx - math.pi

    front_idx = round(n_lasers / 2) + 1

    # Prepare message for the robot's motors
    linear_vel: float
    angular_vel: float

    # Decide the robot's behavior
    # TODO

    #ω = dir * distP * (dist_min - wallDist) + angleP * (angle_min - dir*pi/2)
    angular_vel = direction * distP * (min_dist - wallDist) + angleP * (angle_min - direction*math.pi/2)
    #pdb.set_trace()
    print(f"p_dist: {direction * distP * (min_dist - wallDist)} | p_teta: {angleP * (angle_min - direction*math.pi/2)}")

    if dist_values[front_idx] <= wallDist:
        linear_vel = 0
        print("TURN")
    elif dist_values[front_idx] < 2*wallDist or min_dist < wallDist*0.75 or min_dist > wallDist*1.25:
        print("SLOW")
        linear_vel = 0.5*maxSpeed
    else:
        print("CRUISE")

        linear_vel = maxSpeed

    print(f"linear_vel: {linear_vel} | angular_vel: {angular_vel}")
    print("--------------------------------")
    return linear_vel, angular_vel

if __name__ == '__main__':
    # Create the Robot instance.
    robot: Robot = Robot()

    timestep: int = int(robot.getBasicTimeStep())  # in ms

    lidar: Lidar = robot.getDevice('lidar')
    lidar.enable(timestep)
    lidar.enablePointCloud()

    # Main loop
    while robot.step(time_step=128) != -1:
        linear_vel, angular_vel = distance_handler(1, lidar.getRangeImage())
        cmd_vel(robot, linear_vel, angular_vel)

