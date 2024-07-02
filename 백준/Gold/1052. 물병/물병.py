def count_max_bottle(num):
    cnt = 0
    while num > 0:
        cnt += num % 2
        num //= 2
    return cnt


N, K = map(int, input().split())
# 목표하는 물병의 갯수가 현재보다 많으면 옮길 필요가 없음
if K >= N:
    print(0)
else:
    now = N
    # 최소 물병 수가 K가 될때까지 반복
    while count_max_bottle(now) > K:
        now += 1
    print(now - N)