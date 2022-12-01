from collections import deque


def bfs(data):
    result = farest_node = 0
    visited = [0]*(n+1)
    visited[data[0]] = 1
    q = deque([data])
    while q:
        root = q.popleft()
        for child in tree[root[0]]:
            if not visited[child[0]]:
                visited[child[0]] = 1
                q.append([child[0], child[1]+root[1]])
                if root[1] + child[1] > result:
                    result = root[1] + child[1]
                    farest_node = child[0]
    return result, farest_node


n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    root, child, w = map(int, input().split(' '))
    tree[root].append([child, w])
    tree[child].append([root, w])

cal_result, cal_far = bfs([1, 0])
final_result, final_node = bfs([cal_far, 0])
print(final_result)
