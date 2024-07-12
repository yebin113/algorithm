import sys

# 입력 받기
G = int(input())

# 성원이의 몸무게**2 리스트
weight_list = []
number = 0

# 1차이 나는 제곱수의 차가 G보다 커질때까지
while number**2 - (number-1)**2 <= G:
    number += 1
    weight_list.append(number**2)

# 투 포인터로 현재 몸무게 찾기
start = 0
end = 1
cnt = 0
while True:
    if start == len(weight_list):
        break
    if weight_list[end] - weight_list[start] == G:
        print(end+1)
        cnt += 1
        start += 1
        end += 1
    elif weight_list[end] - weight_list[start] < G and end < len(weight_list)-1:
        end += 1
    else:
        start += 1

# 가능한 몸무게가 없을 때
if cnt == 0:
    print(-1)