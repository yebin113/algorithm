N = int(input())
dp = [N]*(N+1)
dp[N] = 0
for i in range(N,0,-1):
    if i * 3 <= N:
        dp[i] = min(dp[i], dp[i*3]+1)
    if i * 2 <= N:
        dp[i] = min(dp[i], dp[i*2]+1)
    if i + 1 <= N:
        dp[i] = min(dp[i],dp[i+1]+1)

print(dp[1])