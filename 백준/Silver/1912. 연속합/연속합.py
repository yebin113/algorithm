n = int(input())
dp = list(map(int, input().split()))
for i in range(1, n):
    # print(dp)
    dp[i] = max(dp[i], dp[i - 1] + dp[i])
# print(dp)dp
print(max(dp))
