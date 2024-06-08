M,N = map(int,input().split())
# 저장, 출력
dp = [[[0] for _ in range(N)] for _ in range(M)]
arr = []
for i in range(M):
    
    line = list(map(int,input()))
    arr.append(line)

max_save = 0
# 열 순서 (왼 -> 오)
for i in range(N):
    # 행 순서 (위 -> 아래)
    for j in range(M):
        # 첫줄인 경우 출력에 가중치만 저장
        if i == 0:
            dp[j][i] = arr[j][i]
        # 그 외는 입력값 + 가중치
        else:
            # 인덱스 오류 방지
            if j == 0:
                dp[j][i] = max(dp[j][i-1], dp[j+1][i-1])
            elif j == M-1:
                dp[j][i] = max(dp[j][i - 1], dp[j - 1][i - 1])
            else:
                dp[j][i] = max(dp[j][i - 1], dp[j - 1][i - 1],dp[j + 1][i - 1])
            max_save = max(max_save,dp[j][i])
            dp[j][i] += arr[j][i]

print(max_save)