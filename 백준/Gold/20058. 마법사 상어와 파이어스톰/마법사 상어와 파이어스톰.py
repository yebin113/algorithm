from collections import deque


def print_arr(arr):
    for i in range(NN):
        print(*arr[i])
    print()


def reduce_ice(arr):
    q = deque()
    for i in range(NN):
        for j in range(NN):
            cnt = 0
            for di, dj in around:
                ni = i + di
                nj = j + dj
                if not (0 <= ni < NN and 0 <= nj < NN) or arr[ni][nj] == 0:
                    continue
                cnt += 1
            if cnt < 3:
                if arr[i][j] == 1:
                    q.append((i, j))
                elif arr[i][j] == 0:
                    continue
                else:
                    arr[i][j] -= 1
    while q:
        x, y = q.popleft()
        arr[x][y] -= 1

    return arr


def rotate_melt(l, arr):
    new_arr = [[0] * (NN) for _ in range(NN)]
    step = 2 ** l
    for origin_j in range(0, NN, step):
        for origin_i in range(0, NN, step):
            for i in range(step):
                for j in range(step):
                    new_arr[origin_j + j][origin_i + step - i - 1] = arr[origin_j + i][origin_i + j]
    new_arr = reduce_ice(new_arr)
    return new_arr


def bfs(i, j):
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    cnt = 1
    while q:
        i,j = q.popleft()
        for di, dj in around:
            ni = i + di
            nj = j + dj
            if not (0 <= ni < NN and 0 <= nj < NN) or board[ni][nj] == 0 or visited[ni][nj] != 0:
                continue
            cnt += 1
            q.append((ni,nj))
            visited[ni][nj] = 1
    return cnt


around = [[0, 1], [-1, 0], [1, 0], [0, -1]]
N, Q = map(int, input().split())
NN = 2 ** N
board = []
for _ in range(NN):
    board.append(list(map(int, input().split())))
orders = list(map(int, input().split()))
for order in orders:
    board = rotate_melt(order, board)

visited = [[0]*NN for _ in range(NN)]
sum_arr = sum(sum(board,[]))
max_cnt = 0
for i in range(NN):
    for j in range(NN):
        if visited[i][j] != 0 or board[i][j] == 0:
            continue
        cnt = bfs(i,j)
        max_cnt = max(max_cnt, cnt)
print(sum_arr)
print(max_cnt)
