# https://school.programmers.co.kr/learn/courses/30/lessons/72413

# sol1: dijkstra
from heapq import heappush, heappop

def solution(n, s, a, b, fares):

    def dijkstra(start):
        INF = int(1e9)
        distance = [INF] * (n+1)
        q = []
        distance[start] = 0
        heappush(q, (0,start))

        while q:
            dist, now = heappop(q)
            if dist > distance[now]:
                continue
            
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heappush(q, (cost, i[0]))
        return distance
    
    graph = [[] for _ in range(n+1)]
    for c, d, f in fares:
        graph[c].append((d,f))
        graph[d].append((c,f))
    
    s_dist = dijkstra(s)
    answer = s_dist[a] + s_dist[b]
    for i in range(1,n+1):
        i_dist = dijkstra(i)
        answer = min(answer, i_dist[a]+i_dist[b]+s_dist[i])
    
    return answer

# sol2: floyd-warshall
def solution(n, s, a, b, fares):
    INF = int(1e9)
    graph = [[INF] * (n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        graph[i][i] = 0
    
    for c, d, f in fares:
        graph[c][d] = f
        graph[d][c] = f
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    answer = INF
    for i in range(1,n+1):
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])
        
    return answer