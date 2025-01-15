# https://www.acmicpc.net/problem/9019
import sys
input = sys.stdin.readline
from collections import deque

def convert(start: int, target: int):
    q = deque([(start, "")])
    visited = [0] * 10000
    visited[start] = 1

    while q:
        n, now = q.popleft()

        if n == target:
            return now
        
        # D
        d_value = (n * 2) % 10000
        if not visited[d_value]:
            visited[d_value] = 1
            q.append((d_value, now + 'D'))

        # S
        s_value = 9999 if n == 0 else n - 1
        if not visited[s_value]:
            visited[s_value] = 1
            q.append((s_value, now + 'S'))

        # L
        l_value = (n % 1000) * 10 + (n // 1000)
        if not visited[l_value]:
            visited[l_value] = 1
            q.append((l_value, now + 'L'))

        # R
        r_value = (n % 10) * 1000 + (n // 10)
        if not visited[r_value]:
            visited[r_value] = 1
            q.append((r_value, now + 'R'))

    
T = int(input())
for _ in range(T):
    n, target = map(int, input().split())
    print(convert(n, target))