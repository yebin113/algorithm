N = int(input())
dp = [0]*(N+1)
graph = [[] for _ in range(N+1)]
for i in range(N):
    arr = list(map(int,input().split()))
    hour = arr.pop(0)
    num = arr.pop(0)
    # 선행관계가 없다면 바로 그 숫자로 저장
    if num == 0:
        dp[i+1] = hour
    else:
        # 선행관계가 있는 것들을 조사
        max_time = 0
        for pre_num in arr:
            max_time = max(max_time,dp[pre_num])
        dp[i+1] = max_time+hour

print(max(dp))
