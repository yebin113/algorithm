from collections import deque
dir = [(0,1), (0,-1), (1,0), (-1,0)]
def bfs(si, sj):
    q = deque([[si, sj]])
    visited[si][sj] = 0
    while q:
        
        i, j = q.popleft()
        for di, dj in dir:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == -1:
                if arr[ni][nj] == "1" or arr[ni][nj] == "#":
                    visited[ni][nj] = visited[i][j] + 1
                    q.append([ni, nj])
                else:
                    visited[ni][nj] = visited[i][j]
                    q.appendleft([ni, nj])



N,M = map(int,input().split())
x1, y1, x2, y2 = map(int,input().split())
arr = []
visited = [[-1]*M for _ in range(N)]
for _ in range(N):
    arr.append(list(input()))

bfs(x1-1, y1-1)
print(visited[x2-1][y2-1])