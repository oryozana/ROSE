
from TempObstacle import *


class TernaryTree:
    steps = 60

    def __init__(self, value, left=None, middle=None, right=None):
        self.left = left
        self.middle = middle
        self.right = right
        self.value = value

    def set_children(self, left, middle, right):
        self.left = left
        self.middle = middle
        self.right = right

    def is_leaf(self):
        return self.right is None and self.middle is None and self.left is None
