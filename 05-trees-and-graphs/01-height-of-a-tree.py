class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def tree_height(n):
    if n is None:
        return 0
    return 1 + max(tree_height(n.left), tree_height(n.right))
