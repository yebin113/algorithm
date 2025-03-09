from collections import deque
def bfs(i, j, h):
    q = deque()
    q.append((i,j))
    while q:
        i,j = q.popleft()
        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            ni = i + di
            nj = j + dj
            if not(0<=ni<N and 0<=nj<N) or visited[ni][nj] or arr[ni][nj] <= h:
                continue
            visited[ni][nj] = 1
            q.append((ni,nj))


N = int(input())
arr = []
numbers = set()
for _ in range(N):
    line = list(map(int,input().split()))
    arr.append(line)
    for i in range(N):
        numbers.add(line[i])
max_safety_zone = 1
for height in numbers:
    safety_zone = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] or arr[i][j] <= height:
                continue
            visited[i][j] = 1
            bfs(i,j,height)
            safety_zone += 1
    max_safety_zone = max(max_safety_zone,safety_zone)
print(max_safety_zone)



