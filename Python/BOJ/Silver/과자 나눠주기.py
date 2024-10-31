# https://www.acmicpc.net/problem/16401
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
L = list(map(int, input().split()))

start, end = 1, max(L)
answer = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in L:
        if i >= mid:
            total += i // mid
    
    if total < M:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid

print(answer)