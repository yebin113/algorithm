from itertools import combinations
def distance():
    min_dis = 10000000
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if i == j or j == k or i == k :
                    continue
                dis = 0
                for m in range(4):
                    if mbti_list[i][m] != mbti_list[j][m]:
                        dis += 1
                    if mbti_list[j][m] != mbti_list[k][m]:
                        dis += 1
                    if mbti_list[i][m] != mbti_list[k][m]:
                        dis += 1
                min_dis = min(min_dis,dis)
    return min_dis



T = int(input())
for _ in range(T):
    N = int(input())
    mbti_list = list(input().split())

    if N > 32:
        print(0)
    else:
        print(distance())
