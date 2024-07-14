n = int(input())
data = list(map(int, input().split()))
dp = [1] * (n+1)
# 증가하는 수열 갯수 기록
for i in range(len(data)):
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
ans = max(dp)
# 결과저장
result = []
# 뒤에서 부터 오면서
for i in range(n-1, -1, -1):
    # 현재 갯수랑 맞는 위치의 숫자 추가
    if dp[i] == ans:
        result.append(data[i])
        ans -= 1

for i in range(len(result)-1,-1,-1):
    print(result[i],end=" ")