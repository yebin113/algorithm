n = int(input())
count_list = [0] * 500001
arr = map(int, input().split())

for i in arr:
    count_list[i] += 1
print(max(count_list))
