from collections import deque


def bfs(i, j, idx):
    """
    주어진 좌표 주변을 돌면서 산봉우리인지 판단
    :param i, j: 현재 위치 
    :param idx: 산봉우리 
    :return: 산봉우리인지 아닌지
    """
    q = deque([(i, j)])
    visited[i][j] = 1
    check = [(i, j)]
    while q:
        i, j = q.popleft()
        for di, dj in around:
            ni, nj = i + di, j + dj
            if not (0 <= ni < N and 0 <= nj < M) or visited[ni][nj]:
                continue
            if farm[i][j] < farm[ni][nj]:
                return False
            if farm[i][j] == farm[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni, nj))
                check.append((ni, nj))
        idx += check
    return True


N, M = map(int, input().split())
farm = []
idx_list = []
for _ in range(N):
    farm.append(list(map(int, input().split())))
around = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]

answer = 0
for i in range(N):
    for j in range(M):
        if (i, j) not in idx_list:
            visited = [[0] * M for _ in range(N)]
            if bfs(i, j, idx_list):
                answer += 1

print(answer)
