import sys

n, m = map(int,sys.stdin.readline().split())
inf = int(1e9)
graph = [[inf]*(n+1) for _ in range(n+1)]
<<<<<<< HEAD

for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:  
            graph[a][b] = 0

=======
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0
>>>>>>> 425949da4c9334f18dc9a3ed566a83e8d5ee8382
for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a][b] = 1

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
<<<<<<< HEAD
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

result = 0
for i in range(1,n+1):
    cnt = 0
    for j in range(1, n+1):
        if graph[i][j] != inf or graph[j][i] != inf:
            cnt += 1
    if cnt == n:
        result += 1
print(result)
=======
            if graph[a][k] + graph[k][b] == 2:
                graph[a][b] = 1

student = 0
for i in range(1,n+1):
    count = 0
    for j in range(1,n+1):
        if graph[i][j] == 1:
            count += 1
        if graph[j][i] == 1:
            count += 1
    if count == n-1:
        student += 1
print(student)
>>>>>>> 425949da4c9334f18dc9a3ed566a83e8d5ee8382
