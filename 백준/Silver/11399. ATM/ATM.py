N = int(input())
arr = list(map(int, input().split()))
arr.sort()
s = 0
for i in range(N):
    s += (N-i) * arr[i]
print(s)