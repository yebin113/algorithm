from collections import deque


def bfs(i, j):
    global max_painting
    visited[i][j] = 1
    q = deque()
    q.append((i, j))
    cnt = 1
    while q:
        # print(q)
        i, j = q.popleft()
        for di, dj in dir:
            ni = i + di
            nj = j + dj
            if not (0 <= ni < n and 0 <= nj < m):
                continue
            if visited[ni][nj]:
                continue
            if arr[ni][nj]:
                visited[ni][nj] = 1
                cnt += 1

                q.append((ni, nj))
    return cnt


n, m = map(int, input().split())
arr = []
dir = [[1, 0], [-1, 0], [0, -1], [0, 1]]
for i in range(n):
    arr.append(list(map(int, input().split())))

max_painting = 0
visited = [[0] * m for _ in range(n)]
cnt_painting = 0
for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue
        if arr[i][j]:
            cnt_painting += 1
            max_painting = max(max_painting,bfs(i, j))
        # print()
        # for k in range(n):
        #     print(visited[k])

print(cnt_painting)
print(max_painting)
