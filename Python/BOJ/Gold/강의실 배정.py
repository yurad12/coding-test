# https://www.acmicpc.net/problem/11000
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input())
courses = [list(map(int, input().split())) for _ in range(N)]

courses.sort(key = lambda x: (x[0],x[1]))
answer = 1
q = []
heappush(q, 0)
for s, t in courses:
    if q[0] <= s:
        heappop(q)
    else:
        answer += 1
    heappush(q, t)

print(answer)