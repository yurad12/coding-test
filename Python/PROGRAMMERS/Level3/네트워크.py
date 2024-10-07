# https://school.programmers.co.kr/learn/courses/30/lessons/43162
'''
bfs로 연결된 노드 찾기 ->  끝나면 네트워크 + 1
'''

from collections import deque

def bfs(i, visited, n, computers):
    q = deque([i])
    while q:
        v = q.popleft()
        for c in range(n):
            if v == c: continue
            if visited[c]: continue
            if computers[v][c]:
                q.append(c)
                visited[c] = 1

def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if visited[i]: continue
        bfs(i, visited, n, computers)
        answer += 1
    return answer