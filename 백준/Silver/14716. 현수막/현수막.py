from collections import deque

def print_arr():
    for i in range(M):
        print(*visited[i],"      ",*banner[i])
    print()

def bfs(i, j):
    global answer

    visited[i][j] = 1
    q = deque()
    q.append((i, j))
    while q:
        i, j = q.popleft()
        for di, dj in around:
            ni = i + di
            nj = j + dj
            if not (0 <= ni < M and 0 <= nj < N) or visited[ni][nj]:
                continue
            visited[ni][nj] = 1
            if banner[ni][nj] == 0:
                continue
            q.append((ni, nj))
    # print_arr()
    answer += 1

around = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
M, N = map(int, input().split())
banner = []
visited = [[0] * N for _ in range(M)]
answer = 0
for _ in range(M):
    banner.append(list(map(int, input().split())))
for i in range(M):
    for j in range(N):
        if visited[i][j] == 0 and banner[i][j]:
            bfs(i, j)
print(answer)