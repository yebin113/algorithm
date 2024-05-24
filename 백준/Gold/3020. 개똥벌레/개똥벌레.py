N, H = map(int, input().split())

# 위에서 내려오는 것과 아래에서 올라가는 것
bottom = [0] * (H + 1)
top = [0] * (H + 1)

min_cnt = N
cnt = 0

# 현재를 입력받아 홀수면 바닥에서 더하고,
# 짝수면 위에서 더함
for i in range(N):
    now = int(input())
    if (i+1) % 2:
        bottom[now] += 1
    else:
        top[now] += 1
# print(top)
# print(bottom)
# 높이가 x이상인 것은 1~x 까지의 모든 경로에 걸림
for i in range(H - 1, 0, -1):
    bottom[i] += bottom[i + 1]
    top[i] += top[i + 1]
# print(top)
# print(bottom)

# 갱신
for i in range(1, H + 1):
    if min_cnt > (bottom[i] + top[H - i + 1]):
        min_cnt = (bottom[i] + top[H - i + 1])
        cnt = 1
    elif min_cnt == (bottom[i] + top[H - i + 1]):
        cnt += 1

print(min_cnt, cnt)