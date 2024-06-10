import heapq
heap = []
N = int(input())
visited = [0]*(1001)
for _ in range(N):
    # d : 과제 마감일까지 남은 일수
    # w : 과제의 점수
    d, w = map(int,input().split())
    heapq.heappush(heap,[-w,d])


while heap:
    # 점수 높은 순으로 뽑기
    minus_now_w,now_d = heapq.heappop(heap)
    now_w = -minus_now_w

    # 현재 마감 기간 부터 0까지 돌면서 가장 마감에 가까운날에 기록
    for i in range(now_d,0,-1):
        if visited[i] != 0:
            continue
        visited[i] = now_w
        break

print(sum(visited))

