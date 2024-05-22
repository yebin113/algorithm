import sys
input=sys.stdin.readline
from collections import defaultdict

while 1:
    n,k = map(int,input().split())
    if n == 0 and k == 0:
        break
    node_list = list(map(int,input().split()))
    parent = defaultdict(int)
    cnt = 0

    now = 0
    # 루트인 1번 이후로 돌면서
    for i in range(1, n):
        # 현재 노드의 값에 현재 저장되어있는 위치의 값을 추가
        parent[node_list[i]] = node_list[now]
        # 만약 마지막 리스트 값이 아니고 연속된 값이 아니면 위치 + 1
        if i < n - 1 and node_list[i] + 1 < node_list[i + 1]:
            now += 1

    # 만약 주어진 k가 존재한다면
    if parent[parent[k]]:
        # 노드 리스트를 돌면서 부모는 다르지만, 부모의 부모가 같다면 수를 + 1
        for node in node_list:
            if (parent[parent[k]] == parent[parent[node]]) and parent[node] != parent[k]:
                cnt += 1
    print(cnt)



