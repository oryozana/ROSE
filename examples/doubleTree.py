import bn as bn


class DoubleTree:
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

        # Print the tree

    def create_tree_print_list(self):
        height = self.getHeight()
        rows = height + 1
        cols = (2 ** (height + 1)) - 1

        our_list = []
        for row in range(rows):
            new_line = []
            for col in range(cols):
                new_line.append("X")
            our_list.append(new_line)
        return our_list

    def create_tree_list(self):  # row = 0, col = 0 at first use.
        tree_list = self.create_tree_print_list()
        tree_list[0][(len(tree_list[0]) - 1) / 2] = self.value.p
        height = self.getHeight()
        return self.add_tree_children_to_tree_list(self, 0, tree_list[0], height, tree_list)

    def add_tree_children_to_tree_list(self, tree: "Tree", row: int, col: int, height: int, tree_list):
        if tree is not None:
            if tree.has_left():
                tree_list[row + 1][col - 2 ** (height - row - 1)] = tree.left.value.p
                tree.left.print_tree_children(tree.left, row + 1, tree_list[row + 1], height, tree_list)
            if tree.has_middle():
                tree_list[row + 1][col] = tree.middle.value.p
                tree.middle.print_tree_children(tree.middle, row + 1, tree_list[row + 1], height, tree_list)
            if tree.has_right():
                tree_list[row + 1][col + 2 ** (height - row - 1)] = tree.right.value.p
                tree.right.print_tree_children(tree.right, row + 1, tree_list[row + 1], height, tree_list)
        return tree_list

    def print_tree_list(self):
        tree_list = self.create_tree_list()
        for row in tree_list:
            print(*row)

    # def checkForBestPattern(self):
    #     h = self.getHeight()
    #     numberOfValues = (3**(h + 1) - 1) / 2
    #     for i in range(numberOfValues):

    def getHeight(self):
        if self is None:
            return 0
        return self.getHeight(self.middle) + 1

    def get_left(self):
        return self.left

    def get_middle(self):
        return self.middle

    def get_right(self):
        return self.right

    def get_value(self):
        return self.value
