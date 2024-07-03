import sys
import heapq
input = sys.stdin.readline

N = int(input())
class_list = []
for _ in range(N):
    class_list.append(list(map(int, input().split())))
class_list.sort(key=lambda x: x[1])

heap = []
cnt = 0
for now_class in class_list:
    while heap and heap[0] <= now_class[1]: 
        heapq.heappop(heap)       
    heapq.heappush(heap, now_class[2])    
    cnt = max(cnt, len(heap))

print(cnt)