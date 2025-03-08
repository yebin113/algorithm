"""
BFS
N개의 정점과 M개의 간선으로 구성된 무방향 그래프
정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1
R에서 시작하여 너비 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력
인접 정점은 오름차순으로 방문
"""
from collections import deque
def bfs(r):
    visited = [0]*(N+1)
    visited[r] = 1
    q = deque()
    q.append(r)
    idx = 1
    while q:
        cur_node = q.popleft()
        for next_node in graph[cur_node]:
            if visited[next_node]:
                continue
            idx += 1
            visited[next_node] = idx
            q.append(next_node)
    return visited

N, M, R = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1,N+1):
    graph[i] = list(sorted(graph[i]))
# print(graph)
visited = bfs(R)
for i in range(1,N+1):
    print(visited[i])

