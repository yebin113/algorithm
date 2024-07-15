import copy


def dfs(man, point):
    global max_point
    if man == 11:
        max_point = max(max_point, point)
        return
    for i in range(11):
        if visited[i] or ability[man][i] == 0:
            continue
        visited[i] = 1
        dfs(man + 1, point + ability[man][i])
        visited[i] = 0


T = int(input())

for _ in range(T):

    max_point = 0
    ability = []
    for _ in range(11):
        C = list(map(int, input().split()))
        ability.append(C)
    visited = [0]*11
    dfs(0, 0)
    print(max_point)
