N = int(input())
dp = [0]*10001
dp[1] = 1
dp[2] = 1
for i in range(3,10001):
    dp[i] = dp[i-1]+dp[i-2]
print(dp[N])