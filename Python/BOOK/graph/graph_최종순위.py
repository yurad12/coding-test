# https://www.acmicpc.net/problem/3665

import sys
input = sys.stdin.readline
from collections import deque

case = int(input())

while case != 0:
    case -= 1
    n = int(input())
    rank = list(map(int,input().split()))
    m = int(input())
    changes = [list(map(int,input().split())) for _ in range(m)]

    # 진입차수, 간선정보 -> 등수가 낮을수록 진입차수 높게
    indegree = [0] * (n+1)
    graph = [[False]*(n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(i+1,n):
            graph[rank[i]][rank[j]] = True
            indegree[rank[j]] += 1
    
    # 바뀐 등수 적용
    for change in changes:
        a, b = change
        if not graph[a][b]:
            indegree[a] -= 1
            indegree[b] += 1
            graph[a][b] = True
            graph[b][a] = False
        else:
            indegree[a] += 1
            indegree[b] -= 1
            graph[a][b] = False
            graph[b][a] = True

    
    # 진입차수가 0인 노드 큐에 삽입
    q = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
    
    # 위상정렬
    result = []
    certainty = True
    cycle = False
    for i in range(n):
        # error 1
        if len(q) > 1:
            certainty = False
            break
        # error 2
        if len(q) == 0:
            cycle = True
            break
        node = q.popleft()
        result.append(node)
        for j in range(1,n+1):
            if graph[node][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if certainty == False:
        print('?')
    elif cycle == True:
        print('IMPOSSIBLE')
    else:
        for result in result:
            print(result, end=' ')
        print()