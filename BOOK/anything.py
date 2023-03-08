from collections import deque
import copy

n = int(input())
time = [0] * (n+1)
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for i in range(1,n+1):
    temp = list(map(int,input().split()))
    time[i] = temp[0]
    for j in temp[1:-1]:
        graph[j].append(i) #i를 수강하려면 j를 수강해야함
        indegree[i] += 1

result = copy.deepcopy(time)
q = deque()
for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    node = q.popleft()
    for i in graph[node]:
        result[i] = max(result[i],result[node]+time[i])
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

for t in range(1,n+1):
    print(result[t])