'''
Bellman Ford
- 음수 최단 경로
'''

v, e, start = map(int, input().split())
INF = int(1e9)
distance = [INF] * (v+1)
edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((a,b,cost))

def bellman_ford(start):
    distance[start] = 0

    for i in range(v):
        for j in range(e):
            a, b, cost = edges[j]
        
            if distance[b] > distance[a] + cost:
                distance[b] = distance[a] + cost
                if i == v - 1:
                    return False
    
    return True

bellman_ford(start)