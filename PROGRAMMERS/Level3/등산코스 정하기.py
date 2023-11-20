# https://school.programmers.co.kr/learn/courses/30/lessons/118669

from heapq import heappush, heappop

INF = int(1e9)
    
def solution(n, paths, gates, summits):
    d = [INF] * (n+1)
    isSummit = [False] * (n+1)
    for summit in summits:
        isSummit[summit] = True
    
    graph = [[] for _ in range(n+1)]
    for a,b,c in paths:
        graph[a].append((b,c))
        graph[b].append((a,c))

    q = []
    for gate in gates:
        d[gate] = 0
        heappush(q, (0, gate))
    
    while q:
        dist, now = heappop(q)
        if d[now] != dist:
            continue
        for i in graph[now]:
            if d[i[0]] <= max(d[now], i[1]):
                continue
            d[i[0]] = max(d[now], i[1])
            if not isSummit[i[0]]:
                heappush(q, (d[i[0]],i[0]))
    
    ans_summit = summits[0]
    for summit in summits:
        if d[summit] < d[ans_summit]:
            ans_summit = summit
        elif d[summit] == d[ans_summit] and summit < ans_summit:
            ans_summit = summit
    
    answer = [ans_summit, d[ans_summit]]

    return answer