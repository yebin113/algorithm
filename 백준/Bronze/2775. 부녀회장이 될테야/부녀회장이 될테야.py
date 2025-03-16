T = int(input())

for _ in range(T):  
    floor = int(input())
    room = int(input())
    arr = [i+1 for i in range(room)]
    for j in range(floor):
        for i in range(1, room):
            arr[i] += arr[i-1]
    print(arr[-1])