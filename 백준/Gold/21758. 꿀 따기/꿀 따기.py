
n = int(input())
m = list(map(int, input().split()))
total_honey = sum(m)
answer = 0
can_not_eat = m[0]

# 벌벌꿀
#  첫 번째와 마지막 벌이 먹는 꿀의 양은 고정
for i in range(1, n):
    # 중간 벌이 못 먹는 꿀의 양
    can_not_eat += m[i]
    # 첫 번째 + 두번째 벌이 먹을 수 있는 꿀의 양
    answer = max(answer, total_honey - m[0] + total_honey - can_not_eat - m[i]) 

# 벌꿀벌
for i in range(1, n):
    # 모든 꿀 다 먹기
    answer = max(answer, total_honey - m[0] - m[-1] + m[i]) 

# 꿀벌벌
m.reverse()
can_not_eat = m[0]
for i in range(1, n):
    can_not_eat += m[i]

    answer = max(answer, total_honey - m[0] + total_honey - can_not_eat - m[i]) 




print(answer)