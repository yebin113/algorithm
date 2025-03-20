n = int(input())
arr = []
for _ in range(n):
    t,p = map(int,input().split())
    arr.append((t,p))

dp = [0]*(n+1)
for i in range(n):
    for j in range(i+arr[i][0],n+1):
        if dp[j] <dp[i] + arr[i][1]:
            dp[j] = dp[i]+arr[i][1]
print(dp[-1])