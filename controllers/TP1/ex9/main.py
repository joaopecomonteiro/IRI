"""
IRI - TP1 - Ex 9
By: Gonçalo Leão
"""
import math
from controller import Robot, Compass
from controllers.utils import cmd_vel

robot: Robot = Robot()

timestep: int = int(robot.getBasicTimeStep())  # in ms
PRINT_AFTER_N_STEPS: int = 20

compass: Compass = robot.getDevice('compass')
compass.enable(timestep)

cmd_vel(robot, 0, math.pi)

print_step: int = 0
while robot.step() != -1:
    print_step += 1
    if print_step % PRINT_AFTER_N_STEPS == 0:
        print(compass.getValues())
        # TODO: Print compass readings
