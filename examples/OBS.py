from rose.common import obstacles, actions  # NOQA

clear = (obstacles.NONE, obstacles.PENGUIN)
notclear = (obstacles.BARRIER, obstacles.BIKE, obstacles.TRASH)
obstacles_dict = {obstacles.NONE: 0,
                  obstacles.TRASH: -10,
                  obstacles.BIKE: -10,
                  obstacles.BARRIER: -10,
                  obstacles.CRACK: 5,
                  obstacles.WATER: 4,
                  obstacles.PENGUIN: 10}


class OBS:
    def __init__(self, x, y, world):
        self.x = x
        self.o = world.get((x, y))
        self.p = obstacles_dict[self.o]

    def set_points(self):
        self.p = 0
        if self.o not in notclear:  # If it is an obstacle.
            self.p = -10
