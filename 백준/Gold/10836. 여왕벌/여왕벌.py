def print_arr(arr):
    for j in range(M):
        print(*arr[j])
    print()

M,N = map(int,input().split())

arr = [[1] * M for _ in range(M)]

# N일 동안
for _ in range(N):
    line = list(map(int,input().split()))
    larva = [0]*line[0]+[1]*line[1]+[2]*line[2]
    # print(larva)
    visited = [[0] * M for _ in range(M)]

    for i in range(len(larva)):
        if i < M:
            arr[M-1-i][0] += larva[i]
            visited[M - 1 - i][0] = larva[i]
        else:
            arr[0][i-M+1] += larva[i]
            visited[0][i-M+1] = larva[i]
    # print_arr(arr)
    # print_arr(visited)
    for i in range(1,M):
        for j in range(1,M):
            arr[i][j] += max(visited[i-1][j-1],visited[i-1][j],visited[i][j-1])
            visited[i][j] = max(visited[i-1][j-1],visited[i-1][j],visited[i][j-1])

print_arr(arr)

