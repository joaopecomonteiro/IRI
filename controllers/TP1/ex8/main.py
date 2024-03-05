"""
IRI - TP1 - Ex 8
By: Gonçalo Leão
"""

from controller import Robot, Lidar, LidarPoint
from controllers.utils import *
PRINT_AFTER_N_STEPS: int = 20
def main():
    #print_devices()

    robot: Robot = Robot()

    timestep: int = int(robot.getBasicTimeStep())  # in ms

    lidar: Lidar = robot.getDevice('lidar')
    lidar.enable(timestep)
    lidar.enablePointCloud()
    #while True:
    #    move_forward(robot, 25 / 100, 0.1)
    #    pc = lidar.getPointCloud()
    #    for point in pc:
    #        print(f"X: {point.x}, Y: {point.y}, Z: {point.z}")
    #    rotate(robot, math.pi / 2, math.pi / 2)
    cmd_vel(robot, 0, 0.3)
    print_step: int = 0
    while robot.step() != -1:
        print_step += 1
        if print_step % PRINT_AFTER_N_STEPS == 0:
            pc = lidar.getPointCloud()
            for point in pc:
                print(f"X: {point.x}, Y: {point.y}, Z: {point.z}")

if __name__ == '__main__':
    main()
