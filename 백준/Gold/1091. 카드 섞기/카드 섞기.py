


N = int(input())
P = list(map(int,input().split()))
S = list(map(int,input().split()))
pattern = []
cards = [0,1,2] * (N//3)
origin = [0,1,2] * (N//3)
cnt = 0
while cards != P:
    cnt += 1
    new_cards = [0] * N
    for i in range(N):
        new_cards[i] = cards[S[i]]
    # print(new_cards, "   ", cards)
    cards = new_cards[:]

    if cards == origin:
        print(-1)
        break
    
else:
    print(cnt)
