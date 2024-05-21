# 부모 찾기 - 가장 최 상단의 부모를 찾는다
def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]

# 병합하기 - 각각의 부모를 찾아 더 작은 수로 통합
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())

graph = []
parent = list(range(N + 1))
for _ in range(M):
    # A,B와 유지보수 비용 
    A_house, B_house, cost = map(int, input().split())
    graph.append((cost, A_house, B_house))
# 유지보수 비용이 작은 순서대로 정렬한다
graph.sort()

total = 0
last = 0
for now_cost, now_a, now_b in graph:
    # a와 b의 마을이 같지 않다면, 유지보수 비용을 추가한다
    if find(now_a) != find(now_b):
        union(now_a, now_b)
        total += now_cost
        # 그리고 마지막 간선을 갱신해준다
        last = now_cost
# 마을을 두개로 분리하기 위해 마지막 간선은 제거해준다
total -= last
print(total)