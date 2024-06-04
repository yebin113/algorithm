from collections import defaultdict
import sys
input = sys.stdin.readline


def dfs(start, now, visited):
    # 현재 방문처리
    visited[now] = True
    # 현재
    for next in graph[now]:
        # 방문 안했을때 방문처리
        if not visited[next]:
            height[start].add(next)
            height[next].add(start)
            # 다음 차례 재귀
            dfs(start, next,visited)



n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

height = defaultdict(set)
ans = 0

# 모든 사람 dfs 순회
for i in range(1, n+1):
    visited = [False] * (n+1)
    dfs(i, i, visited)

for i in range(1, n+1):
    if len(height[i]) == n-1:
        ans += 1
print(ans)