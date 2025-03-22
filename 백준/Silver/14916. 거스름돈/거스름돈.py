n = int(input())
dp = [1e9]*(n+1)
for i in range(2,n+1):
    if i%2 == 0:
        dp[i] = i//2
    if i%5 == 0:
        dp[i] = i//5

for i in range(3,n+1):
    if i >= 5:
        dp[i] = min(dp[i], dp[i-5]+1, dp[i-2]+1)
    dp[i] = min(dp[i],dp[i-2]+1)
    # print(dp)

if dp[n] > n:
    print(-1)
else:
    print(dp[n])
    