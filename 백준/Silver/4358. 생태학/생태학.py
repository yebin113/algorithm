# import sys
# input = sys.stdin.readline
dictionary = {}
cnt = 0
while True:
    try:
        a = input()


        cnt += 1
        if a in dictionary:
            dictionary[a] += 1
        else:
            dictionary[a] = 1
    except:
        break
    # print(a)

sorted_list = list(dictionary.keys())
sorted_list.sort()
for d in sorted_list:
    print(f'{d} {(dictionary[d]/cnt)*100:.4f}')