N, K = map(int,input().split())
dp = [[1]*(i+1) for i in range(N)]
# for i in range(N):
#     print(dp[i])
for i in range(1,N):
    for j in range(1,i):
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
print(dp[N-1][K-1])
