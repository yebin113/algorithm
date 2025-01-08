def f():
    check = 0
    if len(ans) == M:
        print(*ans)
        return
    for i in range(N):
        if check != num_list[i] and visited[i] == 0:
            ans.append(num_list[i])
            visited[i] = 1
            check = num_list[i]
            f()
            ans.pop()
            visited[i] = 0


N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
visited = [0] * N
ans = []
f()