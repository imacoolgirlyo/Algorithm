tree = {}
n = int(input())
level_min = [n]
level_max = [0]
x = 1
root = 0
level_depth = 1


class Node:
    def __init__(self, data, left_node, right_node):
        self.parent = -1
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


def in_order(node, level):
    global level_depth, x
    level_depth = max(level_depth, level)
    if node.left_node != -1:
        in_order(node.left_node, level+1)
    level_min[level] = min(level_min[level], x)
    level_max[level] = max(level_max[level], x)

    x += 1
    if node.right_node != -1:
        in_order(node.right_node, level+1)


for i in range(1, n+1):
    tree[i] = Node(i, -1, -1)
    level_min.append(n)
    level_max.append(0)


for _ in range(n):
    data, left_node, right_node = map(int, input().split())
    tree[data].left_node = left_node
    tree[data].right_node = right_node
    if left_node != -1:
        tree[left_node].parent = data
    if right_node != -1:
        tree[right_node].parent = data


for i in range(1, n+1):
    if tree[i].parent == -1:
        root = i

in_order(tree[root], 1)

result_level = 1
result_width = level_max[1]-level_max[1]+1

for i in range(2, level_depth+1):
    width = level_max[i]-level_min[i]+1
    if result_width < width:
        result_level = i
        result_width = width
