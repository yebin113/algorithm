def check_line(line):
    global cnt
    start = line[0]
    now = 1
    flag = False
    for i in range(1,N):
        try:
            if line[i-1] == line[i+1] and line[i-1] > line[i]:
                return
        except:
            pass

        # 2칸 이상 차이나면 바로 끝
        if abs(line[i]-start) > 1:
            # print("2칸 이상 차이")
            return
        # 같은 높이인 경우 경사로 놓일 공간 +
        elif line[i] == start:
            now += 1
            # 만약 경사로를 세우는 상황이였고 경사로가 놓일 자리가 생겼다면 초기화
            if flag and now >= L:
                flag = False
                now = 0

        # 올라가는 경사로가 필요한 경우
        elif line[i] > start:
            # 경사로를 세우는 상황이 아니고 경사로 놓일 자리가 있다면 세우기
            if flag == False and now >= L:
                flag = False
                now = 1
            # 그 외는 안됨
            else:
                # print("올라가다가 오류가 남",i)
                return
            start = line[i]
        # 내려가는 경사로가 필요한 경우
        elif line[i] < start:
            # 이미 경사로 세우고 있었으면 안됨
            if flag:
                # print("내려가다가 오류가 남", i)
                return
            now = 1
            start = line[i]
            if L == 1:
                continue
            flag = True
    if flag:
        return
    # print("통과", line)
    cnt += 1



N, L = map(int,input().split())
arr = []
cnt = 0
for _ in range(N):
    arr.append(list(map(int,input().split())))
for i in range(N):
    vertical_line = []
    horizontal_line = []
    for j in range(N):
        vertical_line.append(arr[i][j])
        horizontal_line.append(arr[j][i])
    # print(vertical_line,horizontal_line)
    check_line(vertical_line)
    check_line(horizontal_line)
print(cnt)
