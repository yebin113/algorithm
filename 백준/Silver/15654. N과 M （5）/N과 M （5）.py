import copy
from sys import stdin

input = stdin.readline


def f(nums, step):
    new_nums = copy.deepcopy(nums)
    if step == M:
        for i in range(M):
            print(numbers[nums.index(i)], end=" ")
        print()
        return
    for i in range(N):
        if nums[i] == -1:
            new_nums[i] = step
            f(new_nums, step + 1)
            new_nums[i] = -1




N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
f([-1] * N, 0)
