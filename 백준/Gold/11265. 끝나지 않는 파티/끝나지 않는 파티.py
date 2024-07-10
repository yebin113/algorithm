N, M = map(int, input().split())
party = []
for i in range(N):
    party.append(list(map(int,input().split())))
    
# 3중 for문을 돌면서
for a in range(N):
    for b in range(N):
        for c in range(N):
            # 만약 b->c 직행보다 a를 거쳐가는게 더 빠르면 교체
            if party[b][c] > party[b][a] + party[a][c]:
                party[b][c] = party[b][a] + party[a][c]

for _ in range(M):
    a, b, time = map(int, input().split())
    a -= 1
    b -= 1
    # 남은 시간과 최적화해둔 루트를 확인
    if party[a][b] <= time:
        print('Enjoy other party')
    else:
        print('Stay here')