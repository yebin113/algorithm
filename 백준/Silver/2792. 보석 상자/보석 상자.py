import sys
input = sys.stdin.readline

N, M = map(int, input().split())
colors = [int(input()) for _ in range(M)]

start = 1
end = max(colors)

while start <= end:
    mid = (start+end) // 2
    sum_jewels = 0
    for color in colors:
        if color % mid:
            sum_jewels += (color//mid) + 1
        else:
            sum_jewels += color//mid
    if sum_jewels > N:
        start = mid + 1

    else:
        end = mid - 1

print(start)