# https://www.acmicpc.net/problem/2304
'''
l이 인덱스, h는 높이
1. 가장 높은 기둥을 기준으로 왼쪽 스택, 오른쪽 스택으로 나누기
2. 왼쪽 스택: 높은 기둥의 높이를 더하기
3. 오른쪽 스택: 역순으로 높은 기둥의 높이 더하기
'''

import sys
input = sys.stdin.readline

n = int(input())
pillars = [0] * 1001
idx, criteria = 0, 0
for _ in range(n):
    l, h = map(int, input().split())
    pillars[l] = h
    if criteria < h:
        idx, criteria = l, h

answer = 0
now = 0
for i in range(idx+1):
    now = max(now, pillars[i])
    answer += now

now = 0
for i in range(1000,idx,-1):
    now = max(now, pillars[i])
    answer += now


print(answer)

