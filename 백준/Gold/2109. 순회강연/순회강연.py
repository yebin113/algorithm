import heapq

n = int(input())
pay_list = []
for _ in range(n):
    p,d = map(int,input().split())
    pay_list.append((d,p))
# 마감 날짜 기준으로 정렬(빠른 날짜 ~ 널널한 날짜)
pay_list.sort()

ans = []
for d,p in pay_list:
    # 일단 돈 정답에 추가
    heapq.heappush(ans,p)
    # 마감일을 넘김
    if (len(ans) > d):
        heapq.heappop(ans)
print(sum(ans))
