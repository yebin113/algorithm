N, M = map(int,input().split())
lectures = list(map(int,input().split()))
start = max(lectures)
end = sum(lectures)
answer = 0

while start <= end:
    mid = (start+end)//2
    cnt = 0
    long = 0
    for i in range(N):

        if long + lectures[i] > mid:
            cnt += 1
            long = 0
        long += lectures[i]

    if long > 0:
        cnt += 1
    # print(f'start {start} end {end} mid {mid} cnt {cnt} M {M}')
    if cnt <= M:
        end = mid - 1
        answer = mid
    else:
        start = mid + 1
print(answer)