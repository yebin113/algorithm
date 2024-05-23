from collections import deque
import sys
input = sys.stdin.readline
#     상  하  좌  우
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]


def move(i, y, di, dj):
    count = 0

    while True:
        if board[i + di][y + dj] == '#' or board[i][y] == 'O':
            return i, y, count

        i += di
        y += dj
        count += 1


def bfs(r,b):
    ri, rj = r
    bi, bj = b
    queue = deque()
    queue.append([ri, rj, bi, bj, 0])

    visited[ri][rj][bi][bj] = True

    while queue:
        ri, rj, bi, bj, count = queue.popleft()

        for i in range(4):
            # 10번 지나면 진행 X
            if count > 10:
                print(0)
                return
            # 현재 위치가 구멍이라면
            if board[ri][rj] == 'O':
                print(1)
                return

            # 네방향으로 이어서 진행
            for i in range(4):
                n_ri, n_rj, rcount = move(ri, rj, di[i], dj[i])
                n_bi, n_bj, bcount = move(bi, bj, di[i], dj[i])

                if board[n_bi][n_bj] == 'O':
                    continue

                if n_ri == n_bi and n_rj == n_bj:
                    if rcount > bcount:
                        n_ri -= di[i]
                        n_rj -= dj[i]
                    else:
                        n_bi -= di[i]
                        n_bj -= dj[i]

                if visited[n_ri][n_rj][n_bi][n_bj] == 0:
                    visited[n_ri][n_rj][n_bi][n_bj] = 1
                    queue.append([n_ri, n_rj, n_bi, n_bj, count + 1])

    print(0)


n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(input().rstrip()))
red =[0,0]
blue = [0,0]
for r in range(n):
    for c in range(m):
        if board[r][c] == 'R':
            red = [r, c]
        if board[r][c] == 'B':
            blue = [r, c]



visited = [[[[0] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
bfs(red,blue)
