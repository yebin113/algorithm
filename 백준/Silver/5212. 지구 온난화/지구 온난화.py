def add_sink():
    for i in range(r):
        for j in range(c):
            if now_map[i][j] == 'X':
                # 바다 개수
                sea_cnt = 0
                for di, dj in around:
                    ni = i + di
                    nj = j + dj
                    # 범위 내일때
                    if 0 <= ni < r and 0 <= nj < c:
                        if now_map[ni][nj] == '.':
                            sea_cnt += 1
                    # 범위 밖이면 무조건 바다
                    else:
                        sea_cnt += 1
                        continue
                if sea_cnt >= 3:
                    sink.append((i, j))

def change_into_sea():
    # 바다로 바꾸기
    if len(sink) > 0:
        for x, y in sink:
            now_map[x][y] = '.'

def find_area():
    # 바다 범위 구하기
    si = 0
    sj = c - 1
    ei = 0
    ej = 0
    # 지도 범위 구하기
    for i in range(0, r):
        if 'X' in now_map[i]:
            si = i
            break
    for i in range(r - 1, -1, -1):
        if 'X' in now_map[i]:
            ei = i
            break

    for i in range(si, ei + 1):
        for j in range(c):
            if now_map[i][j] == 'X':
                sj = min(sj, j)
                ej = max(ej, j)
    return si,sj,ei,ej


around = [[0, 1], [-1, 0], [1, 0], [0, -1]]
r,c = map(int,input().split())
now_map = [list(input()) for _ in range(r)]
sink = []
# 가라앉은 곳 추가
add_sink()
# 바다로 바꾸기
change_into_sea()
# 바다 범위 구하기
si,sj,ei,ej = find_area()

for i in range(si, ei + 1):
    for j in range(sj, ej + 1):
        print(now_map[i][j], end='')
    print()
