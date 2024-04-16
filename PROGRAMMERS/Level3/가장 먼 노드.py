# https://school.programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    visited = [-1] * (n+1)
    
    q = deque([1])
    visited[1] = 0
    
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] > -1:
                continue
            # 1에서 제일 가까운 것부터 탐색하니까 거리를 비교해줄 필요 없음
            visited[i] = visited[v]+1
            q.append(i)
    max_dist = max(visited)
    return visited.count(max_dist)