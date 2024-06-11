import sys
input = sys.stdin.readline

M,N = map(int,input().split())

arr = [[1] * M for _ in range(M)]
larva = [1]*(2*M-1)
# N일 동안 애벌레 자란거 적립
for _ in range(N):
    one,two,three = list(map(int,input().split()))
    two += one
    three += two
    for i in range(2*M-1):
        if one <= i < two:
            larva[i] += 1
        elif i >= two:
            larva[i] += 2

# 왼쪽, 위쪽 줄을 토대로 전체 애벌레 결과 
# 첫번째 숫자는 수열에서 가져오기, 2~M까지는 맨 윗줄의 수 가져오기(증가하는 수이기 때문에 맨 윗줄이 가장 큰 수임)
for i in range(M):
    print(larva[M-1-i],*larva[M:])
