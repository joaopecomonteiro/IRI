"""
IRI - TP4 - Ex 2
By: Gonçalo Leão
"""
import math
from typing import Union, Tuple

from matplotlib import pyplot as plt

from controller import Robot, Lidar, LidarPoint, Compass, GPS, Keyboard
import numpy as np

from controllers.TP4.occupancy_grid import OccupancyGrid
from controllers.transformations import create_tf_matrix, get_translation
from controllers.utils import cmd_vel, bresenham_extended

import os
os.environ["WEBOTS_HOME"] = "/usr/local/webots"

class ProbabilisticOccupancyGrid(OccupancyGrid):
    def __init__(self, origin: (float, float), dimensions: (int, int), resolution: float):
        super().__init__(origin, dimensions, resolution)

        # Initialize the grid
        self.log_prior = self.get_log_odd(0.5)
        #self.occupancy_grid: np.ndarray  # TODO
        self.occupancy_grid = np.ones(shape=self.dimensions) * 0.5

    def update_map(self, robot_tf: np.ndarray, lidar_points: [LidarPoint]) -> None:
        # Get the grid coord for the robot pose
        #robot_coord: (int, int)  # TODO
        robot_coord = self.real_to_grid_coords(get_translation(robot_tf))

        # Get the grid coords and distances for the lidar points
        grid_lidar_coords: [(int, int)] = []
        measured_dists: [float] = []
        for point in lidar_points:
            coords = robot_tf @ np.array([point.x, point.y, 0, 1])
            grid_point = self.real_to_grid_coords(coords)

            dist = math.sqrt((coords[0] - robot_coord[0]) ** 2 + (coords[1] - robot_coord[1]) ** 2)

            bre_points = bresenham_extended(robot_coord, coords, (0, 0), self.dimensions)
            for bre_point in bre_points[1:-1]:
                self.update_cell(bre_point, False)
            self.update_cell(grid_point, True)
        self.update_cell(robot_coord, False)
        # Update the cell of the robot's position
        # TODO

        # Update the cells on the lines defined by the lidar points
        # TODO

    def update_cell(self, coords: (int, int), is_robot_cell: bool, cell_minus_measured_distance_to_robot: float) -> None:
        if self.are_grid_coords_in_bounds(coords):
            # Update the grid cell
            inverse_sensor_model_prob: float = 0.1
            if not is_robot_cell:
                inverse_sensor_model_prob = ...  # TODO
            self.occupancy_grid[coords] = ...  # TODO

    def get_probability_grid(self) -> np.ndarray:
        # TODO
        pass

    def get_log_odd(self, prob: float) -> float:
        # TODO
        pass


def main() -> None:
    robot: Robot = Robot()
    timestep: int = 100  # in ms

    kb: Keyboard = Keyboard()
    kb.enable(timestep)

    keyboard_linear_vel: float = 0.3
    keyboard_angular_vel: float = 1.5

    map: ProbabilisticOccupancyGrid = ProbabilisticOccupancyGrid([0.0, 0.0], [200, 200], 0.01)

    lidar: Lidar = robot.getDevice('lidar')
    lidar.enable(timestep)
    lidar.enablePointCloud()

    compass: Compass = robot.getDevice('compass')
    compass.enable(timestep)

    gps: GPS = robot.getDevice('gps')
    gps.enable(timestep)

    scan_count: int = 0
    while robot.step(timestep) != -1:
        key: int = kb.getKey()
        if key == ord('W'):
            cmd_vel(robot, keyboard_linear_vel, 0)
        elif key == ord('S'):
            cmd_vel(robot, -keyboard_linear_vel, 0)
        elif key == ord('A'):
            cmd_vel(robot, 0, keyboard_angular_vel)
        elif key == ord('D'):
            cmd_vel(robot, 0, -keyboard_angular_vel)
        else:  # Not a movement key
            cmd_vel(robot, 0, 0)
            if key == ord(' '):
                scan_count += 1
                print('scan count: ', scan_count)

                # Read the robot's pose
                gps_readings: [float] = gps.getValues()
                robot_position: (float, float) = (gps_readings[0], gps_readings[1])
                compass_readings: [float] = compass.getValues()
                robot_orientation: float = math.atan2(compass_readings[0], compass_readings[1])
                robot_tf: np.ndarray = create_tf_matrix((robot_position[0], robot_position[1], 0.0), robot_orientation)

                # Read the LiDAR and update the map
                map.update_map(robot_tf, lidar.getPointCloud())

                # Show the updated map
                plt.imshow(np.flip(map.get_probability_grid(), 0))
                plt.savefig('ex2-scan' + str(scan_count) + '.png')
                # plt.show()


if __name__ == '__main__':
    main()
