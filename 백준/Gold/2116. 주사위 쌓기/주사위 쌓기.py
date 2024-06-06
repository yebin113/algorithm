N = int(input())
# 반댓면
dice_locate = {
    0: 5,
    1: 3,
    2: 4,
    3: 1,
    4: 2,
    5: 0,
}
# 각 인덱스에서의 옆면 인덱스
sides = [[1, 2, 3, 4], [0, 2, 4, 5], [0, 1, 3, 5], [0, 2, 4, 5], [0, 1, 3, 5], [1, 2, 3, 4]]
dices = []
for _ in range(N):
    dices.append(list(map(int, input().split())))

max_sum = 0
# 맨 밑 주사위 6면 다 해보기
for i in range(6):
    bottom_idx = i
    top_idx = dice_locate[bottom_idx]
    bottom_num = dices[0][bottom_idx]
    top_num = dices[0][top_idx]

    sum_side = 0

    for j in range(N):
        # 현재 주사위
        now_dice = dices[j]
        # 현재 주사위의 가장 큰 옆 수
        max_side_num = 0
        for k in sides[top_idx]:
            max_side_num = max(max_side_num, now_dice[k])
        sum_side += max_side_num
        if j == N-1:
            continue
        # 다음 수
        bottom_idx = dices[j+1].index(top_num)
        top_idx = dice_locate[bottom_idx]
        bottom_num = dices[j+1][bottom_idx]
        top_num = dices[j+1][top_idx]
    max_sum = max(max_sum,sum_side)
print(max_sum)
