n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n):
    # 현재 집이 빨간색일때, 이전 집이 초록색(1)이나 파란색(2)일때의 최솟값에 현재 값을 더해줌
    arr[i][0] = min(arr[i - 1][1], arr[i - 1][2]) + arr[i][0]
    # 현재 집이 초록일때, 이전 집이 빨간색(0)이나 파란색(2)일때의 최솟값에 현재 값을 더해줌
    arr[i][1] = min(arr[i - 1][0], arr[i - 1][2]) + arr[i][1]
    # 현재 집이 파랑일때, 이전 집이 빨간색(0)이나 초록색(`)일때의 최솟값에 현재 값을 더해줌
    arr[i][2] = min(arr[i - 1][0], arr[i - 1][1]) + arr[i][2]

# 빨강, 초록, 파랑으로 시작한 경우의 수중에 가장 작은 경우가 답
print(min(arr[n - 1][0], arr[n - 1][1], arr[n - 1][2]))
