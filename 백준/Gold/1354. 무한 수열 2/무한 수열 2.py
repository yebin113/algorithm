
def get(n, p, q, x, y, dp):
    """
    무한 수열 2의 n번째 항을 계산하여 반환
    """
    if n <= 0:
        return 1
    if n in dp:
        return dp[n]
    dp[n] = get(n // p - x, p, q, x, y, dp) + get(n // q - y, p, q, x, y, dp)
    return dp[n]


N,P,Q,X,Y = map(int, input().split())
dp = {}
print(get(N,P,Q,X,Y, dp))
