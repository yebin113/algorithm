def solution(s):
    stack = []
    
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(s[i])
        else:
            if len(stack) and stack[-1] == "(":
                stack.pop()
            else:
                return False
    if len(stack):
        return False

    return True