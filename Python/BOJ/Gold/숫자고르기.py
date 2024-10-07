# https://www.acmicpc.net/problem/2668
'''
1. 방문한 좌표, 사이클 발생 -> answer에 추가
2. 방문하지 않은 좌표 -> 탐색
'''

import sys
input = sys.stdin.readline

n = int(input())
nums = [0] + list(int(input()) for _ in range(n))

def dfs(v, i):
    visited[v] = 1
    nx = nums[v]

    if visited[nx] and nx == i:
        answer.append(nx)
    elif not visited[nx]:
        dfs(nx,i)

answer = []
for i in range(1,n+1):
    visited = [0] * (n+1)
    dfs(i,i)

print(len(answer))
answer.sort()
for ans in answer:
    print(ans)
