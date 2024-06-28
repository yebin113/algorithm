import heapq
"""
다익스트라 사용
완전 탐색 하면서 가장 짧은 루트를 찾아 출력함
"""
def find_shortest_way(s):
    parents = {}
    for i in range(1, n + 1):
        parents[i] = i
    heap = [10000000] * (n + 1)
    heap[s] = 0

    q = []
    heapq.heappush(q, (0, s))
    while q:
        weight, now_idx = heapq.heappop(q)
        # 이미 방문한 적이 있다면 무시
        if heap[now_idx] < weight:
            continue

        for w,idx in graph[now_idx]:
            next_weight = w
            next_idx = idx
            # 지금 + 다음 길이보다 저장되어있는 길이가 더 짧다면 힙에 추가
            if weight + next_weight < heap[next_idx]:
                heapq.heappush(q, (weight + next_weight, next_idx))
                heap[next_idx] = weight + next_weight
                parents[next_idx] = now_idx
    # 첫번째로 방문하는 곳 출력
    for i in range(1, n + 1):
        # 자기 자신일 경우 -
        if i == s:
            print("-", end=" ")
        else:
            now_i = i
            # parents에서 이전에 들렀던 곳이 시작점과 같아질때까지
            while parents[now_i] != s:
                now_i = parents[now_i]
            print(str(now_i), end=" ")
    print()


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, time = map(int, input().split())
    graph[a].append((time, b))
    graph[b].append((time, a))

for i in range(1, n + 1):
    find_shortest_way(i)