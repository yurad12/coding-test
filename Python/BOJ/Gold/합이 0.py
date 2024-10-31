# https://www.acmicpc.net/problem/3151
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# sol1: Python
A.sort()
answer = 0
count = [0] * 40001

for i in range(N):
    answer += count[20000 - A[i]]
    for j in range(i):
        count[20000 + A[i] + A[j]] += 1

print(answer)

# sol2: PyPy
import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

A.sort()
answer = 0

for i in range(N-2):
    start, end = i+1, N-1

    while start < end:
        total = A[i] + A[start] + A[end]
        if total > 0:
            end -= 1
        else:
            if total == 0:
                if A[start] == A[end]:
                    answer += (end - start)
                else:
                    idx = bisect_left(A, A[end])
                    answer += (end - idx + 1)
            start += 1

print(answer)