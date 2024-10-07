# https://www.acmicpc.net/problem/14888
import sys
from collections import deque
from itertools import permutations

n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
operations = list(map(int,sys.stdin.readline().split()))
ops = []
key = ['+','-','*','/']
# print(nums)
# print(operations)
for i in range(4):
    for _ in range(operations[i]):
        ops.append(key[i])
ops_combination = list(permutations(ops))
# print(ops)

def bfs(nums, ops):
    queue = deque()
    for i in range(len(ops)):
        queue.append((nums[i+1],ops[i]))
    result = nums[0]

    while queue:
        num, op = queue.popleft()
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
        else:
            if result < 0:
                result = -((-result)//num)
            else:
                result = result // num
        # print(result)
    return result

max_num = int(-1e9)
min_num = int(1e9)
for ops in ops_combination:
    res = int(bfs(nums, ops))
    max_num = max(max_num, res)
    min_num = min(min_num, res)
print(max_num, min_num, sep='\n')