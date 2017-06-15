class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def preorder_traversal(node):
    if not node:
        return

    print(node.data)

    preorder_traversal(node.left)
    preorder_traversal(node.right)

def inorder_traversal(node):
    if not node:
        return

    preorder_traversal(node.left)

    print(node.data)

    preorder_traversal(node.right)

def postorder_traversal(node):
    if not node:
        return

    preorder_traversal(node.left)
    preorder_traversal(node.right)

    print(node.data)
    