N = int(input())
numbers = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        # 감소하면 현재 수 + 값 갱신
        if numbers[j] > numbers[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
