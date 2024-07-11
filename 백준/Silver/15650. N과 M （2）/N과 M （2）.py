from itertools import combinations
N,M = map(int,input().split())
numbers = [i for i in range(1,N+1)]
for nums in combinations(numbers,M):
    print(*nums)
