arr = []
while True:
    try:
        a = int(input())
        arr.append(a)
    except:
        break
arr.sort()
print(arr[len(arr)//2])