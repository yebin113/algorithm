T = int(input())

for _ in range(T):
    rect = {
        "left_x": 0,
        "right_x": 0,
        "top_y": 0,
        "bottom_y": 0,
    }
    locate = [0, 0]
    # y축 상숭 -> x축 상승 -> y축 하강 -> x축 하강
    dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    d = 0
    orders = list(input())
    for o in orders:
        # F: 한 눈금 앞으로
        if o == "F":
            locate[0] += dir[d][0]
            locate[1] += dir[d][1]
        # B: 한 눈금 뒤로
        elif o == "B":
            locate[0] -= dir[d][0]
            locate[1] -= dir[d][1]
        # L: 왼쪽으로 90도 회전
        elif o == "L":
            if d == 0:
                d = 3
            else:
                d -= 1
        # R: 오른쪽으로 90도 회전
        elif o == "R":
            if d == 3:
                d = 0
            else:
                d += 1
        # 갱신

        rect["left_x"] = min(rect["left_x"],locate[0])
        rect["right_x"] = max(rect["right_x"], locate[0])
        rect["bottom_y"] = min(rect["bottom_y"], locate[1])
        rect["top_y"] = max(rect["top_y"], locate[1])

    print((rect["right_x"]-rect["left_x"]) * (rect["top_y"]-rect["bottom_y"]))