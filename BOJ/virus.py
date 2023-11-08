## 라이브러리
from collections import deque

## 입력받기
# x:노드 개수, y:쌍 개수
x = int(input())
y = int(input())
graph = [list(map(int, input().split())) for _ in range(y)]
#print(graph)

visited = [False]*(x+1)

## 변환
dic_graph = dict()
for a,b in graph:
    if a not in dic_graph:
        dic_graph[a] = [b]
    else:
        dic_graph[a].append(b)
    if b not in dic_graph:
        dic_graph[b] = [a]
    else:
        dic_graph[b].append(a)
    #dic_graph[a].append(b) if (a in dic_graph) else (dic_graph[a] = b)
    #dic_graph[b].append(a) if (b in dic_graph) else (dic_graph[b] = a)
#print(dic_graph)

## BFS Algorithm
def bfs(graph,start,visited):
    queue = deque([start])
    visited[start] = True
    deque_list = []

    while queue:
        next = queue.popleft()
        deque_list.append(next)
        for i in graph[next]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
    print(len(deque_list)-1)

## 결과
bfs(dic_graph,1,visited)