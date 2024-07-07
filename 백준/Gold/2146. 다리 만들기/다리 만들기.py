import sys
from collections import deque

imput = sys.stdin.readline


def marking(j, i, mark):
    q = deque()
    q.append((j, i))
    sea[j][i] = mark
    visited[j][i] = True
    while q:
        i, j = q.popleft()
        for dj, di in around:
            ni, nj = i + dj, j + di
            if not (0 <= ni < N and 0 <= nj < N) or visited[ni][nj] or not sea[ni][nj]:
                continue
            sea[ni][nj] = mark
            visited[ni][nj] = True
            q.append((ni, nj))


def distance(j, i, now):
    # 좌표에서 가장 가까운 다른 섬의 거리를 구하는 함수
    q = deque()
    q.append((j, i, 0))
    while q:
        i, j, cnt = q.popleft()
        if sea[i][j] != 0 and sea[i][j] != now:
            return cnt
        for dj, di in around:
            ni, nj = i + dj, j + di
            if not (0 <= ni < N and 0 <= nj < N) or visited[ni][nj] or sea[ni][nj] == now:
                continue
            visited[ni][nj] = True
            q.append((ni, nj, cnt + 1))
    return 2000


N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

around = [[0, 1], [0, -1], [1, 0], [-1, 0]]

mark = 1
for i in range(N):
    for j in range(N):
        if sea[i][j] and not visited[i][j]:
            marking(i, j, mark)
            mark += 1

ans = 2000
for i in range(N):
    for j in range(N):
        if sea[i][j] == 0:
            continue
        visited = [[False] * N for _ in range(N)]
        dis = distance(i, j, sea[i][j])
        ans = min(ans, dis)

print(ans - 1)
