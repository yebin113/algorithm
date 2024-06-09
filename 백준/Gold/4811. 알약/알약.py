dp = [[0 for _ in range(31)] for _ in range(31) ]

for j in range(1,31):
    dp[0][j] = 1

for i in range(1,31):
    for j in range(30):

        if j == 0:
            # 반쪽 없을때 => h 무조건 생김
            dp[i][j] = dp[i-1][j+1]
            
        else:
            # 반쪽 있을때 => h 를 먹을 때와  w 를 먹을 때 두가지 경우
            dp[i][j] = dp[i-1][j+1] + dp[i][j-1]



while True:
    N = int(input())
    if N == 0:
        break
    print(dp[N][0])