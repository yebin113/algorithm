T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int,input().split()))
    M = int(input())
    dp = [0 for _ in range(M+1)]
    dp[0] = 1
    for i in range(N):
        now_coin = coins[i]
        for j in range(now_coin,M+1):
            dp[j] += dp[j-now_coin]
    print(dp[-1])