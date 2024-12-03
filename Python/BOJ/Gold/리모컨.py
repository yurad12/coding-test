# https://www.acmicpc.net/problem/1107
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
if M:
    broken = set(map(int, input().split()))
else:
    broken = set()

answer = abs(100 - N)
for i in range(500000*2+1):
    now = str(i)
    for j in range(len(now)):
        if int(now[j]) in broken:
            break
        if j == len(now)-1:
            answer = min(answer, len(now) + abs(i - N))

print(answer)
