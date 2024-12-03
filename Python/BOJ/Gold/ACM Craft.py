# https://www.acmicpc.net/problem/1005
import sys
input = sys.stdin.readline
from collections import deque

def solution(N, K, time, indegree, graph, w):
    q = deque()
    cost = [0] * (N+1)

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append((i, time[i]))
            cost[i] = time[i]

    while q:
        node, t = q.popleft()
        if node == w:
            break
        
        for i in graph[node]:
            indegree[i] -= 1
            cost[i] = max(cost[i], t + time[i])

            if not indegree[i]:
                q.append((i, cost[i]))

    return cost[w]

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    indegree = [0] * (N+1)
    graph = [[] for _ in range(N+1)]
    for _ in range(K):
        x, y = map(int, input().split())
        indegree[y] += 1
        graph[x].append(y)
    
    w = int(input())

    print(solution(N, K, time, indegree, graph, w))
