# https://www.acmicpc.net/problem/4196
import sys
input = sys.stdin.readline

T = int(input())
answer = []

def dfs(now):
    global id
    print("dfs:", now, id)

    stack.append(now)
    visited[now] = id
    now_id = id

    for next in graph[now]:
        if not visited[next]:
            id += 1
            dfs(next)
        if visited[next] <= now_id:
            indegree[next] -= 1
            visited[now] = min(visited[now], visited[next])
    
    if visited[now] == now_id:
        scc.append([])
        sccindegree.append(0)

        while stack:
            x = stack.pop()
            scc[-1].append(x)
            sccindegree[-1] += indegree[x]
            visited[x] = int(1e9)
            if x == now:
                break
    print(sccindegree)
    print(scc)

for _ in range(T):
    N, M = map(int, input().split())
    domino = [list(map(int, input().split())) for _ in range(M)]
    
    indegree = [0] * (N+1)
    graph = [[] for _ in range(N+1)]

    for a, b in domino:
        graph[a].append(b)
        indegree[b] += 1
    
    visited = [0] * (N+1)
    stack = []
    scc = []
    sccindegree = []

    for i in range(1, N+1):
        if not visited[i]:
            id = 1
            dfs(i)

    answer.append(sccindegree.count(0))

for ans in answer:
    print(ans)