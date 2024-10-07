# https://www.acmicpc.net/problem/20055

'''
1. 로봇 올리는 위치에 올리기 또는 이동하면 벨트 내구도-1
2. n에 있으면 내리기
3. 로봇 스스로 이동 가능
'''

import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))

robots = deque([0]*n)
result = 0

while True:
    # 1. 벨트, 로봇 한 칸 회전
    belt.rotate(1)
    robots.rotate(1)
    robots[-1] = 0
    
    # 2. 로봇 이동
    if sum(robots):
        for i in range(n-2, -1, -1):
            if robots[i] and not robots[i+1] and belt[i+1] >= 1:
                robots[i], robots[i+1] = 0, 1
                belt[i+1] -= 1
        robots[-1] = 0
    # 3. 로봇 올리기
    if belt[0] > 0:
        robots[0] = 1
        belt[0] -= 1
    result += 1

    if belt.count(0) >= k:
        break
print(result)
