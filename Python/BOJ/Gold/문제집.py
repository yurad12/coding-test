# https://www.acmicpc.net/problem/1766
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N, M = map(int, input().split())
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    indegree[b] += 1
    graph[a].append(b)

q = []
visited = [0] * (N+1)
for i in range(1, N+1):
    if not indegree[i]:
        heappush(q, i)
        visited[i] = 1

while q:
    x = heappop(q)
    print(x, end = ' ')

    for i in graph[x]:
        if visited[i]:
            continue

        indegree[i] -= 1
        if not indegree[i]:
            heappush(q, i)

print()

'''
6 6
6 5
6 4
5 3
4 2
3 1
2 1

출력 : 6 5 3 4 2 1
정답 : 6 4 2 5 3 1

5 3
4 1
3 1
5 3
-> 2 4 5 3 1

4 2
1 4
3 2
-> 1 3 2 4
'''