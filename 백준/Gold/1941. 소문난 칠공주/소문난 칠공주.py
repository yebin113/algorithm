from collections import deque
from itertools import combinations
around = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_near(arr):
    """
    is_near : 7명의 조합이 인접하고 있는지 판단하는 함수
    
    visited는 7개의 인덱스로 방문여부를 판단
    0번째 인덱스의 i,j 로 시작하여서 델타탐색으로 인접한 자리가 arr에 존재한다면
    해당 인덱스의 i,j 를 q에 넣고 방문처리한다
    visited를 모두 돈다면 True, 아니면 인접하지 않은 자리가 있다고 판단하여 False
    
    :param arr: 7명 자리 배치도 
    :return: 인접여부 True/ False
    """
    visited = [0]*7
    q = deque()
    q.append(arr[0])
    visited[0] = 1
    while q:
        i,j = q.popleft()
        for di, dj in around:
            ni = i + di
            nj = j + dj
            if (ni,nj) in arr:
                next_idx = arr.index((ni,nj))
                if visited[next_idx]:
                    continue
                q.append((ni,nj))
                visited[next_idx] = 1
    if sum(visited) == 7:
        return True
    else:
        return False


def check_SY_cnt(arr):
    """
    이다솜 파과 임도연 파의 비율이 알맞은지 판단하는 함수
    주어진 조합에서 이다솜파가 4명 이상일 때만 True를 리턴한다
    :param arr: 주어진 조합
    :return: 알맞은 조건일 때 True,아니면 False
    """
    S_cnt = 0
    Y_cnt = 0
    for i,j in arr:
        if class_seats[i][j] == "S":
            S_cnt += 1
        else:
            Y_cnt += 1
        # 임도연파가 3명이 넘으면 안됨
        if Y_cnt > 3:
            return False
    return True

class_seats = [list(input()) for _ in range(5)]
seats = [(i,j) for i in range(5) for j in range(5)]
answer = 0
for comb in combinations(seats, 7):
    if check_SY_cnt(comb) and is_near(comb):
        answer += 1
print(answer)