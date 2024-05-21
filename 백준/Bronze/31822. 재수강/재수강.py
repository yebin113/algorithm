code = input()
cnt = 0
t = int(input())
for _ in range(t):
    a = input()
    if (a[:5]==code[:5]):
        cnt += 1
print(cnt)