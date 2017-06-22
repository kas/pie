class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def find_lowest_common_ancestor(root, node1_value, node2_value):
    lowest_common_ancestor = root

    found_least_common_ancestor = False

    while not found_least_common_ancestor and lowest_common_ancestor:
        if node1_value < root.data and node2_value < root.data:
            lowest_common_ancestor = root.left
        elif node1_value > root.data and node2_value > root.data:
            lowest_common_ancestor = root.right
        else:
            found_least_common_ancestor = True

    return lowest_common_ancestor
