def dfs(now_idx, step):
    # 방문처리 후 다음 인덱스를 확인
    visited[now_idx] = True
    next_idx = data[now_idx]
    # 다음 인덱스가 방문되어있지 않은 경우 재귀
    if not visited[next_idx]:
        dfs(next_idx, step)
    # 다음인덱스를 방문했고, 사이클이 발생했다면 결과에 추가
    elif visited[next_idx] and next_idx == step:
        result.append(next_idx)


N = int(input())
data = [0] + [int(input()) for _ in range(N)]
result = []
for i in range(1, N + 1):
    visited = [False] * (N + 1)
    dfs(i, i)
print(len(result))
result.sort()
for i in result:
    print(i)
