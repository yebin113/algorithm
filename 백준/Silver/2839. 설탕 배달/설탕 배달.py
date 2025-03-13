N = int(input())
dp = [-1]*(N+1)
for i in range(N+1):
    if i % 15 == 0:
        dp[i] = i // 5
    elif i % 5 == 0:
        dp[i] = i // 5
    elif i % 3 == 0:
        dp[i] = i // 3

for i in range(3,N+1):
    if i < 5:
        if dp[i-3] == -1:
            continue
        dp[i] = dp[i-3] + 1
    else:
        if dp[i - 3] == -1 or dp[i-5]==-1:
            continue
        elif dp[i - 3] == -1:
            dp[i] = dp[i-5] + 1
        elif dp[i - 5] == -1:
            dp[i] = dp[i - 3] + 1
        else:
            dp[i] = min(dp[i - 3], dp[i-5]) + 1
print(dp[N])



