import copy
from collections import deque


def bfs():
    q = deque()
    visited = [0] * (F + 1)
    visited[S] = 1
    q.append((S, 0))
    while q:
        x, step = q.popleft()
        if x == G:
            return step
        for dx in [U, -D]:
            nx = x + dx
            if not (0 < nx <= F):
                continue
            if visited[nx] == 0 or (visited[nx] and visited[nx] > step + 1):
                visited[nx] = step + 1
                q.append((nx, step + 1))

    return "use the stairs"


F, S, G, U, D = map(int, input().split())

print(bfs())
