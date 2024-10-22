# https://www.acmicpc.net/problem/1931
import sys
input = sys.stdin.readline

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]

sorted_meetings = sorted(meetings, key = lambda x: (x[1], x[0]))

now = 0
answer = 0
for start, end in sorted_meetings:
    if start >= now:
        answer += 1
        now = end

print(answer)