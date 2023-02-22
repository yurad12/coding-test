import sys, copy
from collections import deque

n = int(sys.stdin.readline())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
time = [0] * (n+1)

for i in range(1,n+1):
    temp = list(map(int,sys.stdin.readline().split()))
    time[i] = temp[0]
    for t in temp[1:-1]:
        indegree[i] += 1
        graph[t].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
<<<<<<< HEAD
=======

>>>>>>> 425949da4c9334f18dc9a3ed566a83e8d5ee8382
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1,n+1):
        print(result[i])

topology_sort()