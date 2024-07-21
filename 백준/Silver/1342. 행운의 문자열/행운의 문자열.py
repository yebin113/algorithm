import math
def dfs(word):
    global ans, answer_len
    if len(word) == N:
        if word not in ans:
            ans.add(word)
        return
    # print(word,visited)
    for i in range(N):
        if visited[i] or S[i] == word[-1]:
            continue
        visited[i] = 1
        dfs(word+S[i])
        visited[i] = 0

S = list(input())
N = len(S)
count_S = [0]*N
for i in range(N):
    count_S[S.index(S[i])] += 1

half = N // 2
if N % 2:
    half += 1
count_S.sort(reverse=True)
if count_S[0] > half:
    # 한 문자가 반 넘으면 0가지수
    print(0)
elif count_S.count(1) == N:
    # 다 1개씩 있으면 N!
    print(math.factorial(N))
else:
    visited = [0]*N
    ans = set()
    for i in range(N):
        visited[i] = 1
        dfs(S[i])
        visited[i] = 0
    print(len(ans))