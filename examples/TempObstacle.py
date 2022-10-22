
from TernaryTree import *
from rose.common import obstacles, actions  # NOQA

side_barriers = (obstacles.WATER, obstacles.CRACK)
obstacles_dict = {obstacles.NONE: 0,
                  obstacles.TRASH: -10,
                  obstacles.BIKE: -10,
                  obstacles.BARRIER: -10,
                  obstacles.CRACK: 5,
                  obstacles.WATER: 4,
                  obstacles.PENGUIN: 10}


class TempObstacle:
    def __init__(self, x: int, y: int, world):
        self.x = x
        self.obstacle = world.get((x, y))
        self.points_value = obstacles_dict[self.obstacle]

    def set_points(self):
        self.points_value = 0
        if self.obstacle in side_barriers:
            self.points_value = -10

    def finish_line(self, current_tree_level: int):
        if TernaryTree.steps - current_tree_level < 0:
            self.points_value = 0
