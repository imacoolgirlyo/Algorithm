from collections import deque
v = int(input())

tree = [[] for _ in range(v+1)]

for _ in range(v):
    node_info = list(map(int, input().split()))
    idx = 0
    for i in range(len(node_info)):
        if i == 0:
            idx = node_info[i]
            continue
        if node_info[i] == -1:
            break
        if i % 2 == 0:
            continue
        tree[idx].append([node_info[i], node_info[i+1]])


def bfs(data):
    global v
    visited = [0]*(v+1)
    weight = [0]*(v+1)

    farest_node = 0
    result = 0
    visited[data] = 1
    q = deque([data])

    while q:
        node = q.popleft()
        for ch in tree[node]:
            value, w = ch
            if not visited[value]:
                visited[value] = 1
                q.append(value)
                weight[value] = weight[node] + w
                if result < weight[value]:
                    result = weight[value]
                    farest_node = value

    return [farest_node, result]


# print(bfs(5))
print(bfs(bfs(1)[0])[1])
