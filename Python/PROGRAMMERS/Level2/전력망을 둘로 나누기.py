'''
https://school.programmers.co.kr/learn/courses/30/lessons/86971

각 전선을 끊어보면서 모두 탐색 -> bfs로 몇 개 연결되는 지 확인
'''
from collections import deque

def bfs(node, visited, wires_graph, links):
    q = deque([node])
    visited[node] = 1
    count = 1
    while q:
        v = q.popleft()
        for i in wires_graph[v]:
            if visited[i] or not links[v][i]:
                continue
            visited[i] = 1
            count += 1
            q.append(i)
    return count
    
def solution(n, wires):
    answer = 100
    wires_graph = [[] for _ in range(n+1)]
    links = [[0] * (n+1) for _ in range(n+1)]
    for v1, v2 in wires:
        wires_graph[v1].append(v2)
        wires_graph[v2].append(v1)
        links[v1][v2] = 1
        links[v2][v1] = 1
    
    for v1, v2 in wires:
        visited = [0] * (n+1)
        links[v1][v2] = 0
        cnt_v1 = bfs(v1, visited, wires_graph, links)
        cnt_v2 = bfs(v2, visited, wires_graph, links)
        links[v1][v2] = 1
        
        answer = min(answer, abs(cnt_v1-cnt_v2))
        
    return answer