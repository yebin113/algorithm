class Robot:
    def __init__(self, x, y, view):
        self.x = x
        self.y = y
        self.view = view
        self.cleaned = 0
        self.is_working = True

    def start(self):
        while self.is_working:
            self.work()

    def work(self):
        # 1. 현재 칸 청소
        if arr[self.x][self.y] == 0:
            self.clean()

        # 2. 주변 4칸 중 청소되지 않은 칸이 없는 경우
        if self.is_near_clean():
            ni = self.x - directions[self.view][0]
            nj = self.y - directions[self.view][1]
            # 벽이면 종료
            if arr[ni][nj] == 1:
                self.is_working = False
                return
            # 후진 가능하면 후진
            self.x, self.y = ni, nj
            return

        # 3. 반시계 방향으로 회전하며 탐색
        for _ in range(4):
            self.view = (self.view - 1) % 4  # 반시계 방향 90도 회전
            ni = self.x + directions[self.view][0]
            nj = self.y + directions[self.view][1]
            if arr[ni][nj] == 0:  # 청소되지 않은 빈 칸이면 이동 후 청소
                self.x, self.y = ni, nj
                return

    def clean(self):
        arr[self.x][self.y] = 2  # 2: 청소 완료
        self.cleaned += 1

    def is_near_clean(self):
        # 4방향 모두 청소되었거나 벽인지 확인
        for di, dj in directions:
            ni, nj = self.x + di, self.y + dj
            if arr[ni][nj] == 0:
                return False  # 청소되지 않은 빈 칸이 있으면 False
        return True  # 모두 청소됨


# 방향: 북(0), 동(1), 남(2), 서(3)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 입력
N, M = map(int, input().split())
r, c, view = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 로봇 청소기 실행
robot = Robot(r, c, view)
robot.start()
print(robot.cleaned)
