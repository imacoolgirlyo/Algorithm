import sys
sys.setrecursionlimit(10**8)

# 어떻게 시간을 줄여야할지 모르겠음;


class Node:
    def __init__(self, n):
        self.data = n
        self.left_node = None
        self.right_node = None


class binarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root == None:
            self.root = Node(key)
        else:
            current = self.root
            while True:
                if current.data > key:
                    # 1) 왼쪽 자식이 있는지 확인 2) 있다면 current 갱신 후 다시 값 비교  3) 없다면 왼쪽 노드로 삽입 시키고 나가기
                    if current.left_node == None:
                        current.left_node = Node(key)
                        break
                    current = current.left_node

                if current.data < key:
                    if current.right_node == None:
                        current.right_node = Node(key)
                        break
                    current = current.right_node

    def postorder(self, node):
        if node.left_node != None:
            self.postorder(node.left_node)
        if node.right_node != None:
            self.postorder(node.right_node)
        print(node.data)
        return


BST = binarySearchTree()

while True:
    try:
        key = int(input())
        BST.insert(key)
    except:
        break

BST.postorder(BST.root)
