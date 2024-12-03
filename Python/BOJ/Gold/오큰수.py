# https://www.acmicpc.net/problem/17298
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

answer = [-1] * N
stack = [A[-1]]

for i in range(N-2, -1, -1):
    while stack and stack[-1] <= A[i]:
        stack.pop()
    
    if stack:
        answer[i] = stack[-1]
    stack.append(A[i])

print(*answer)
