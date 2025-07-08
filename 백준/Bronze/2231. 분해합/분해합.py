n = int(input())

for i in range(1,n+1):
    added_num = i
    str_i = str(i)
    for num_i in str_i:
        added_num += int(num_i)
    if added_num == n:
        print(i)
        break
else:
    print(0)