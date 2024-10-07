# https://www.acmicpc.net/problem/1966

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
while n > 0:
    n -= 1
    m, target = map(int, input().split())
    temp = list(map(int, input().split()))
    q = deque()

    for i in range(m):
        q.append((i, temp[i]))

    temp.sort()

    print_cnt, max_score = 0, temp[-1]

    while True:
        now, score = q.popleft()
        if score == max_score:
            if now == target:
                break
            temp.pop()
            max_score = temp[-1]
            print_cnt += 1
        else:
            q.append((now, score))

    print(print_cnt+1)
