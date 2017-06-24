def traverse(node, count, node_list):
    if not node:
        return count

    if node_list:
        node_list[count] = node

    count += 1

    count = traverse(node.left, count, node_list)
    count = traverse(node.right, count, node_list)

    return count


def heapify_binary_tree(root):
    node = None
    node_list = []

    traverse(root, 0, node_list)

    node_list.sort()

    for i in range(0, len(node_list)):
        left = 2*i + 1
        right = left + 1


        if left >= len(node_list):
            node_list[i].left = None
        else:
            node_list[i].left = node_list[left]

        if right >= len(node_list):
            node_list[i].right = None
        else:
            node_list[i].right = node_list[right]

    return node_list[0]
