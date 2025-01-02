import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def dfs(parent):
    for child in tree[parent]:
        if ans[child] != -1:
            continue
        ans[child] = parent
        dfs(child)


N = int(input())
tree = [[] for _ in range(N)]
ans = [-1] * (N)
for _ in range(N - 1):
    a, b = map(int, input().split())
    a-=1
    b-=1
    tree[a].append(b)
    tree[b].append(a)
dfs(0)
for i in range(1, N):
    print(ans[i]+1)
