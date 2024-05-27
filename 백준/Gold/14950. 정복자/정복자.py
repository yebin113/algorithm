
import heapq

def bfs():
    answer, cnt = 0, 0
    visited = [0] * (n+1)
    visited[1] = 1
    q = []
    for next_road, c in graph[1]:
        heapq.heappush(q,(c,next_road))
    while q:
        cost, w = heapq.heappop(q)
        if visited[w]: continue
        visited[w] = 1
        answer += cost + (cnt * t)
        cnt += 1
        for next_road, c in graph[w]:
            if not visited[next_road]:
                heapq.heappush(q,(c, next_road))
    return answer

n, m, t = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


print(bfs())