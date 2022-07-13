import random
from xmlrpc.client import TRANSPORT_ERROR
from rose.common import obstacles, actions  # NOQA

driver_name = "Moshiko Boozaglo"


# def use(x, y, front, obstacle0, obstacle1, obstacle2, obstacle, use_action):


USABLES = [obstacles.PENGUIN, obstacles.WATER, obstacles.CRACK]
UNUSABLES = [obstacles.BARRIER, obstacles.TRASH, obstacles.BIKE]
ACTIONS = [actions.PICKUP, actions.BRAKE, actions.JUMP]
def drive(world):
    
    x = world.car.x
    y = world.car.y
    layer1 = world.get((x, y - 1))
    layer2 = [world.get((0, y - 2)), world.get((1, y - 2)), world.get((2, y - 2))]
    layer3 = [world.get((0, y - 3)), world.get((1, y - 3)), world.get((2, y - 3))]
    
    if layer1 in UNUSABLES:
        if x % 3 == 2:
            return actions.LEFT
        if x % 3 == 0:
            return actions.RIGHT
    
    if layer1 in USABLES:
        return ACTIONS[USABLES.index(layer1)]
   
    for pickup in layer2:
        if pickup in USABLES:
            if abs((x % 3) - layer2.index(pickup)) == 1: # layer2.index(pickup) represents the x value of the pickup
                if x % 3 == 0:
                    return actions.RIGHT
                if x % 3 == 2:
                    return actions.LEFT
                if layer2.index(pickup) == 0:
                    return actions.LEFT
                if layer2.index(pickup) == 2:
                    return actions.RIGHT
    
    for pickup in layer3:
        if pickup in USABLES:
            if abs((x % 3) - layer3.index(pickup)) == 2:
                if x % 3 == 0:
                    return actions.RIGHT
                if x % 3 == 2:
                    return actions.LEFT
                
    return actions.NONE
                
    