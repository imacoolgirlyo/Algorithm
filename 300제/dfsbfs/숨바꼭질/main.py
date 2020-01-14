from collections import deque

n, k = map(int, input().split())
arr = [0]*100001


def bfs():
    q = deque([n])

    while q:
        cur_pos = q.popleft()
        if cur_pos == k:
            return arr[cur_pos]
        for next_pos in (cur_pos-1, cur_pos+1, cur_pos*2):
            if 0 <= next_pos <= 100000 and arr[next_pos] == 0:
                arr[next_pos] = arr[cur_pos] + 1
                q.append(next_pos)


print(bfs())
