from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    q = deque()
    q.append((0,0))
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    dir = [[0,1],[1,0],[0,-1],[-1,0]]
    min_root = n*m *100
    while q:
        i,j = q.popleft()
        if i == n-1 and j == m-1:
            min_root = min(min_root, visited[i][j])
            break
        for di, dj in dir:
            ni = i + di
            nj = j + dj
            if not(0<= ni<n and 0<= nj < m):
                continue
            if not(maps[ni][nj]):
                continue
            if not(visited[ni][nj]) or visited[ni][nj] > visited[i][j] + 1:
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni,nj))
                
                
    if min_root == n*m *100:
        min_root = -1
        
    return min_root
