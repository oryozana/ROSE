class Tree:
    index = 0

    def __init__(self, value, left, middle, right):
        self.right = right
        self.middle = middle
        self.left = left
        self.value = value
        self.index += 1

    def __init__(self, value):
        self.right = None
        self.left = None
        self.middle = None
        self.value = value
        self.index += 1

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None

    def has_middle(self):
        return self.middle is not None
