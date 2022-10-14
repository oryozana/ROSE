class Tree:
    def _init_(self, value, left=None, middle=None, right=None):
        self.left = left
        self.middle = middle
        self.right = right
        self.value = value

    def setAll(self,l,m,r):
        self.right = r
        self.middle = m
        self.left = l

    def isleaf(self):
        if self.right is None and self.middle is None and self.left is None:
            return True
        return False