# https://www.acmicpc.net/problem/11780
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
bus = [list(map(int, input().split())) for _ in range(m)]
INF = int(1e9)

dist = [[INF] * (n+1) for _ in range(n+1)]
route = [[[] for _ in range(n+1)] for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            dist[a][b] = 0
            route[a][b] = [0]

for a, b, cost in bus:
    if dist[a][b] < cost:
        continue
    dist[a][b] = cost
    route[a][b] = [a, b]

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            cost = dist[a][k] + dist[k][b]
            if dist[a][b] > cost:
                dist[a][b] = cost
                route[a][b] = route[a][k] + route[k][b][1:]

# print("---answer---")
for d in dist[1:]:
    for i in d[1:]:
        if i == INF:
            print(0, end = ' ')
        else:
            print(i, end = ' ')
    print()

# print("---route---")
for r in route[1:]:
    for i in r[1:]:
        if not i or not i[0]:
            print(0)
        else:
            print(len(i), end = ' ')
            print(*i)