import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
S, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
ans = 0

for _ in range(M):
    h1, h2, k = map(int, input().split())
    graph[h1].append((h2, k))
    graph[h2].append((h1, k))


start = 1
end = 1000000
# 이분 탐색 -> 최대 무게 범위를 맞춰가기
while start <= end:
    mid = (start + end) // 2
    check = False
    visit = [0]*(N+1)
    q = deque()
    q.append(S)
    visit[S] = 1
    while q:
        now = q.popleft()
        # 도착하면 체크
        if now == E:
            check = True
            break
        for next_idx, next_weight in graph[now]:
            # mid 보다 적은 루트는 넘기기
            if visit[next_idx] or next_weight < mid:
                continue
            q.append(next_idx)
            visit[next_idx] = True
    # 갱신
    if check:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)