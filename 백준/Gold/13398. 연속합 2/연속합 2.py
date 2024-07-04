import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
dp = [[num for num in numbers] for _ in range(2)]

for i in range(1, N):
    # 이전 연속된 배열 합과, 현재를 비교
    dp[0][i] = max(dp[0][i - 1] + numbers[i], dp[0][i])
    # 연속된 배열과, 제거된 수열을 비교
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + numbers[i])

print(max(max(dp[0]), max(dp[1])))