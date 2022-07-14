class Tree:
    index = 0

    def __init__(self, value, left=None, middle=None, right=None):
        self.right = right
        self.middle = middle
        self.left = left
        self.value = value
        self.index += 1

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None

    def has_middle(self):
        return self.middle is not None
