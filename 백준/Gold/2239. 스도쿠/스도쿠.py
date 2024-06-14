from sys import stdin
input = stdin.readline

# 맞는 위치인지 확인하는 함수
def check(si, sj, num):
    # 행
    for j in range(9):
        if arr[si][j] == num:
            return False
    # 열
    for i in range(9):
        if arr[i][sj] == num:
            return False
    # 3*3
    ni = (si // 3) * 3
    nj = (sj // 3) * 3
    for l in range(3):
        for m in range(3):
            if arr[ni + l][nj + m] == num:
                return False
    return True

# 맞는 위치에 숫자를 삽입하는 함수
def insert_number(step):
    # 0을 모두 채웠으면 답을 print 한 뒤 모든 함수를 종료
    if step == len(zero_idx):
        for i in range(9):
            for j in range(9):
                print(arr[i][j], end="")
            print()
        exit()

    # 다음 0의 위치 탐방
    ni, nj = zero_idx[step]
    # 1~9까지 넣을 숫자 대입
    for k in range(1, 10):
        # 조건 만족시 숫자 삽입
        if check(ni, nj, k):
            arr[ni][nj] = k
            insert_number(step + 1)
            arr[ni][nj] = 0


arr = []
zero_idx = []
for i in range(9):
    arr.append(list(map(int, input().rstrip())))
    for j in range(9):
        # 0의 위치 저장
        if arr[i][j] == 0:
            zero_idx.append((i, j))
insert_number(0)