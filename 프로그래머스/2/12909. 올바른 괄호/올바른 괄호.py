def solution(s):
    answer = True
    if s[-1] == "(" or s[0] == ")":
        return False
    open = 0
    for i in range(len(s)):
        if s[i] == "(":
            open += 1
        else:
            open -= 1
        if open < 0:
            
            return False
    
    if open == 0:
        return True
    else:
        return False