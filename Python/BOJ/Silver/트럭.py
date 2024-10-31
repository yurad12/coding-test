# https://www.acmicpc.net/problem/13335
import sys
input = sys.stdin.readline
from collections import deque

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

answer = 0
bridge = deque([0] * w)
now = 0

for t in trucks:
    while True:
        answer += 1
        now -= bridge.popleft()

        if now + t <= L:
            now += t
            bridge.append(t)
            break
        else:
            bridge.append(0)

answer += w
print(answer)