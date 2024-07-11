
def dfs(start):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return

    for i in range(start, n + 1):
        ans.append(i)
        dfs(i)
        ans.pop()


n, m = map(int, input().split())

ans = []


dfs(1)