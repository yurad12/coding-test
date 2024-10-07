# https://www.acmicpc.net/problem/17615
'''
case1,2: red, blue -> move red or blue
case3,4: blue, red -> move red or blue
최솟값
- 왼쪽으로 옮기고 싶으면, 가장 왼쪽거부터 옮기기
- 오른쪽으로 옮기고 싶으면 가장 오른쪽거부터 옮기기
'''

import sys
input = sys.stdin.readline

n = int(input())
balls = input().strip()

answer = n

c1 = balls.lstrip('R')
answer = min(answer, c1.count('R'))

c2 = balls.lstrip('B')
answer = min(answer, c2.count('B'))

c3 = balls[::-1].lstrip('R')
answer = min(answer, c3.count('R'))

c4 = balls[::-1].lstrip('B')
answer = min(answer, c4.count('B'))

print(answer)
