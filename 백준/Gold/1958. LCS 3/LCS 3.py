a = [0]+ list(input())
b = [0]+list(input())
c = [0]+list(input())

# i가 a, j가 b, k가 c의 순서가 되기 위해 c가 낮은 차원으로 
dp = [[[0 for _ in range(len(c)+1)] for _ in range(len(b)+1)]
      for _ in range(len(a)+1)]
# 문자열을 순회하며
for i in range(1, len(a)):
    for j in range(1, len(b)):
        for k in range(1, len(c)):
            # 셋다 같은 글자 발견시 +1
            if a[i] == b[j] == c[k]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            # 아니면 세개 중 큰 값으로 갱신
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(dp[-2][-2][-2])