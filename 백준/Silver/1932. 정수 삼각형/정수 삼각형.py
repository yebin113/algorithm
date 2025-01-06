N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(1,N):
    for j in range(len(arr[i])):
        # 첫번째 줄이라면 위에줄 그대로
        if j == 0:
            arr[i][j] = arr[i-1][j] + arr[i][j]
        elif j == len(arr[i])-1:
            arr[i][j] = arr[i-1][j-1] + arr[i][j]
        else:
            arr[i][j] = max(arr[i - 1][j - 1] + arr[i][j],arr[i - 1][j] + arr[i][j])
print(max(arr[-1]))