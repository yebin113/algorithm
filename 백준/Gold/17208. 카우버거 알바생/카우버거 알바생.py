import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
order = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
dp = [[[0]*(K + 1) for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(1, N+1):
    hamburger, french_fri = order[i]
    for j in range(1, M + 1):
        for k in range(1, K + 1):
            # 현재주문 포함한거, 미포함한 것 중 더 큰거로 갱신
            if hamburger <= j and french_fri <= k:
                dp[i][j][k] = max(1 + dp[i - 1][j - hamburger][k - french_fri],dp[i - 1][j][k])
            else:
                dp[i][j][k] = dp[i - 1][j][k]

print(dp[N][M][K])