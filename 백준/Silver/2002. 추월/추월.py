N = int(input())
answer = 0
enter = {}
# 나오는 차량
out = []
# 들어간 순서 저장
for i in range(N):
    car = input()
    enter[car] = i
# 나오는 차량 순서 저장
for _ in range(N):
    car = input()
    out.append(car)

# 나오는 차량 순회
for i in range(N - 1):
    for j in range(i + 1, N):
        # 만약 들어간 순서보다 나온 순서가 더 빠르다면 추월차량 + 1
        if enter[out[i]] > enter[out[j]]:
            answer += 1
            break
print(answer)