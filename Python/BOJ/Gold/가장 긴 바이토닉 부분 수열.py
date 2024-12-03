# https://www.acmicpc.net/problem/11054
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

left = [1] * N
right = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            left[i] = max(left[i], left[j] + 1)

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if A[i] > A[j]:
            right[i] = max(right[i], right[j] + 1)

answer = max(max(left), max(right))
for i in range(N):
    for j in range(i, N-1):
        answer = max(answer, left[i] + right[j] - 1)

print(answer)
