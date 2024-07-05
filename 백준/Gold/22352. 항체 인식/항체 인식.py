from collections import deque
import sys

input = sys.stdin.readline

around = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M = map(int, input().split())
before = [list(map(int, input().split())) for _ in range(N)]
after = [list(map(int, input().split())) for _ in range(N)]


def bfs(s, p, x, y):
    q = deque()
    q.append([x, y])
    before[x][y] = p
    while q:
        i, j = q.popleft()
        for di, dj in around:
            ni = i + di
            nj = j + dj
            if not (0 <= ni < N and 0 <= nj < M):
                continue
            if before[ni][nj] == s:
                before[ni][nj] = p
                q.append([ni, nj])


check = False
for i in range(N):
    for j in range(M):
        if before[i][j] != after[i][j]:
            bfs(before[i][j], after[i][j], i, j)
            check = True
            break
    if check == True:
        break

for i in range(N):
    for j in range(M):
        if before[i][j] != after[i][j]:
            print('NO')
            exit(0)

print('YES')


