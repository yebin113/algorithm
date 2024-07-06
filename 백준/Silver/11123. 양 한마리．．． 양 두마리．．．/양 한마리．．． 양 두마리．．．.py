from collections import deque

around = [[0, 1], [1, 0], [-1, 0], [0, -1]]


def bfs(i, j):
    global cnt
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.popleft()
        for di, dj in around:
            ni = i + di
            nj = j + dj
            if not (0 <= ni < H and 0 <= nj < W) or visited[ni][nj] == 1 or arr[ni][nj] == ".":
                continue
            q.append((ni,nj))
            visited[ni][nj] = 1
    cnt += 1


T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    cnt = 0
    arr = []
    for _ in range(H):
        arr.append(list(input()))
    visited = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if visited[i][j] or arr[i][j] == ".":
                continue
            bfs(i,j)
    print(cnt)