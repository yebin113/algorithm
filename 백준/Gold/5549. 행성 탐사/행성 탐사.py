import sys
input = sys.stdin.readline
M, N = map(int, input().split())
K = int(input())
maps = []
for _ in range(M):
    maps.append(list(input()))

# 정글, 바다, 얼음을 dp로 저장
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(M)]

# 정글 J 바다 O 얼음 I
for i in range(M):
    for j in range(N):
        now_map = maps[i][j]
        if i > 0 and j > 0:
            # 정글, 바다, 얼음을 누적
            for k in range(3):
                dp[i][j][k] = dp[i][j - 1][k] + dp[i - 1][j][k] - dp[i - 1][j - 1][k]
            # 현재 값을 추가
        elif i == 0 and j > 0:
            for k in range(3):
                dp[i][j][k] = dp[i][j - 1][k]
        elif i > 0 and j == 0:
            for k in range(3):
                dp[i][j][k] = dp[i - 1][j][k]
        # 둘다 0일 경우만 1로 초기화
        elif i == 0 and j == 0:
            if now_map == 'J':
                dp[i][j][0] = 1
            elif now_map == 'O':
                dp[i][j][1] = 1
            elif now_map == 'I':
                dp[i][j][2] = 1
            continue
        else:
            continue
        # 현재값 추가
        if now_map == 'J':
            dp[i][j][0] += 1
        elif now_map == 'O':
            dp[i][j][1] += 1
        elif now_map == 'I':
            dp[i][j][2] += 1

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    answer = []
    # 둘다 0의 좌표인 경우에는 현재의 값만
    if x1 == 0 and y1 == 0:
        for k in range(3):
            answer.append(dp[x2][y2][k])
    elif x1 != 0 and y1 == 0:
        for k in range(3):
            answer.append(dp[x2][y2][k] - dp[x1 - 1][y2][k])
    elif x1 == 0 and y1 != 0:
        for k in range(3):
            answer.append(dp[x2][y2][k] - dp[x2][y1 - 1][k])
    elif x1 != 0 and y1 != 0:
        for k in range(3):
            answer.append(dp[x2][y2][k] - dp[x1 - 1][y2][k] - dp[x2][y1 - 1][k] + dp[x1 - 1][y1 - 1][k])
    print(*answer)
