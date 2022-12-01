n = int(input())
tree = {}  # 트리를 dict로 구현


class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


def pre_order(node):
    print(node.data, end='')
    if node.left_node != '.':
        pre_order(tree[node.left_node])
    if node.right_node != '.':
        pre_order(tree[node.right_node])


def in_order(node):
    if node.left_node != '.':
        pre_order(tree[node.left_node])
        print(node.data, end='')
    if node.right_node != '.':
        pre_order(tree[node.right_node])


def post_order(node):
    if node.left_node != '.':
        pre_order(tree[node.left_node])
    if node.right_node != '.':
        pre_order(tree[node.right_node])
    print(node.data, end='')


for _ in range(n):
    data, left_node, right_node = input().split()
    tree[data] = Node(data, left_node, right_node)


pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
