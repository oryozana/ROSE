class Tree:
    def __init__(self, value, index, left, middle, right):
        self.right = right
        self.middle = middle
        self.left = left
        self.index = index
        self.value = value

    def __init__(self, value, index):
        self.right = None
        self.left = None
        self.middle = None
        self.index = index
        self.value = value

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None

    def has_middle(self):
        return self.middle is not None
