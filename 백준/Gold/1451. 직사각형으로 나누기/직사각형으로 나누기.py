import sys
input = sys.stdin.readline

def box_area(si, sj, ei, ej):
    total = 0
    for i in range(si, ei+1):
        for j in range(sj, ej+1):
            total += arr[i][j]
    return total

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
max_multiple = 0

# 1. 세로 3개
for i in range(1, M-1):
    for j in range(i+1, M):
        left = box_area(0, 0, N-1, i-1)
        middle = box_area(0, i, N-1, j-1)
        right = box_area(0, j, N-1, M-1)
        area = left * middle * right
        max_multiple = max(max_multiple, area)

# 2. 가로 3개
for i in range(1, N-1):
    for j in range(i+1, N):
        top = box_area(0, 0, i-1, M-1)
        middle = box_area(i, 0, j-1, M-1)
        bottom = box_area(j, 0, N-1, M-1)
        area = top * middle * bottom
        max_multiple = max(max_multiple, area)

# 3. 가로줄 + 세로 2개
# 4. 세로 2개 + 가로줄
for i in range(1, N):
    top_1 = box_area(0, 0, i-1, M-1)
    bottom_2 = box_area(i, 0, N-1, M-1)
    for j in range(1, M):
        left_1 = box_area(i, 0, N-1, j-1)
        right_1 = box_area(i, j, N-1, M-1)
        area_1 = left_1 * right_1 * top_1

        left_2 = box_area(0, 0, i-1, j-1)
        right_2 = box_area(0, j, i-1, M-1)
        area_2 = left_2 * right_2 * bottom_2
        max_multiple = max(max_multiple, area_1, area_2)

# 5. 가로 2개 + 세로줄
# 6. 세로줄 + 가로 2개
for i in range(1, M):
    left = box_area(0, 0, N-1, i-1)
    right = box_area(0, i, N-1, M-1)
    for j in range(1, N):
        top_1 = box_area(0, i, j-1, M-1)
        bottom_1 = box_area(j, i, N-1, M-1)
        area_1 = left * top_1 * bottom_1

        top_2 = box_area(0, 0, j-1, i-1)
        bottom_2 = box_area(j, 0, N-1, i-1)
        area_2 = right * top_2 * bottom_2
        max_multiple = max(max_multiple, area_1, area_2)

print(max_multiple)
