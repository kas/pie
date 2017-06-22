class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

class NodeStack:
    def __init__(self):
        self.stack = []

    def push(self, node):
        self.stack.insert(0, node)

    def pop(self):
        return self.stack.pop(0)

def preorder_traversal_no_recursion(root):
    node_stack = NodeStack()

    node_stack.push(root)

    while node_stack.stack:
        node = node_stack.pop()

        print(node)

        if node.right:
            node_stack.push(node.right)
        
        if node.left:
            node_stack.push(node.left)
