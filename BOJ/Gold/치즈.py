# https://www.acmicpc.net/problem/27531
# 사이클

import sys
input = sys.stdin.readline

INF = int(1e9)
N = int(input())
edges = [(0,0,0)]
for _ in range(N):
    a, b, p = map(int, input().split())
    edges.append((a,b,p))
edges.sort(key = lambda x: (x[0],[1],[2]))

# 연결된 노드 모두 방문
def dfs(edges, visited, costs, start):
    stack = [start]
    while stack:
        node = stack.pop()
        if visited[node]:
            continue

        visited[node] = True
        costs.append(edges[node][2])
        next_node = edges[node][1]
        if not visited[next_node]:
            stack.append(next_node)

# 사이클 내의 최소 비용 계산
# 상점 1개 -> 치즈 2개
def calc(costs):
    # 0: 이전x현재x 1: 이전o현재x, 2:이전x현재o 3:이전o현재o
    dp = [0, INF, INF, costs[0]]
    # 0:현재x->이전o, 1:현재o->이전x/o, 2:현재x->이전o, 3:현재o->이전x/o
    for cost in costs[1:]:
        new_dp = [INF] * 4
        new_dp[0] = dp[1]
        new_dp[1] = min(dp[0], dp[1]) + cost
        new_dp[2] = dp[3]
        new_dp[3] = min(dp[2], dp[3]) + cost
        dp = new_dp
    return min(dp[1:])

visited = [False] * (N+1)
answer = 0

for i in range(1, N+1):
    if not visited[i]:
        costs = []
        dfs(edges, visited, costs, i)
        answer += calc(costs)

print(answer)
