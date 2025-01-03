N = int(input())

for _ in range(N):
    susic = list(map(str,input().split()))
    start = int(susic[0])
    end = int(susic[-1])
    func = ""
    for i in range(1,len(susic)-1):
        try:
            func_num = int(susic[i])
            if func == "*":
                start *= func_num
            elif func == "+":
                start += func_num
            elif func == "-":
                start -= func_num
            elif func == "/":
                start //= func_num

        except Exception as e:
            func = susic[i]
    if int(start) == int(end):
        print("correct")
    else:
        print("wrong answer")
