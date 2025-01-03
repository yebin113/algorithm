from collections import deque


def twice(num):
    return num * 2


def add_one(num):
    return num * 10 + 1


def bfs(s, e):
    q = deque()
    q.append((s, 1))
    while q:
        # print(q)
        cur, step = q.popleft()
        if cur == e:
            return step
        if twice(cur) <= e:
            q.append((twice(cur), step + 1))
        if add_one(cur) <= e:
            q.append((add_one(cur), step + 1))
    return -1

A, B = map(int, input().split())
if A > B:
    print(-1)
else:
    print(bfs(A,B))