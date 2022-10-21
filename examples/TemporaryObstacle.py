
from rose.common import obstacles, actions  # NOQA

barriers = (obstacles.BARRIER, obstacles.BIKE, obstacles.TRASH)  # come back to fix its name later...
obstacles_dict = {obstacles.NONE: 0,
                  obstacles.TRASH: -10,
                  obstacles.BIKE: -10,
                  obstacles.BARRIER: -10,
                  obstacles.CRACK: 5,
                  obstacles.WATER: 4,
                  obstacles.PENGUIN: 10}


class TemporaryObstacle:
    def __init__(self, x: int, y: int, world):
        self.x = x
        self.obstacle = world.get((x, y))
        self.points_value = obstacles_dict[self.obstacle]

    def set_points(self):
        self.points_value = 0
        if self.obstacle not in barriers:  # If it is an obstacle.
            self.points_value = -10
