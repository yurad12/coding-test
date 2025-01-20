# https://www.acmicpc.net/problem/1744
import sys
input = sys.stdin.readline

N = int(input())
arr = list(int(input()) for _ in range(N))

p_stack, n_stack = [], []
zero = 0
for num in arr:
    if num > 0:
        p_stack.append(num)
    elif num < 0:
        n_stack.append(num)
    else:
        zero += 1
p_stack.sort()
n_stack.sort(reverse=True)

answer = 0

while len(p_stack) > 1:
    x = p_stack.pop()
    y = p_stack.pop()
    answer += max(x + y, x * y)

if p_stack:
    answer += p_stack.pop()

while len(n_stack) > 1:
    x = n_stack.pop()
    y = n_stack.pop()
    answer += (x * y)

if n_stack and not zero:
    answer += n_stack.pop()

print(answer)
