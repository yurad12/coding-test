import sys
input = sys.stdin.readline


def dfs(v, traced):
    global result
    print(v, traced)
    
    visited[v] = True
    traced.append(v)
    nx = students[v]

    if visited[nx]:
        if nx in traced:
            result -= (len(traced)-traced.index(nx))
            return
    else:
        dfs(nx,traced)

t = int(input())
answer = []
while t:
    t -= 1
    n = int(input())
    students = [0] + list(map(int,input().split()))
    visited = [False] * (n+1)
    result = n

    for i in range(1,n+1):
        if not visited[i]:
            dfs(i, [])
    answer.append(result)

for ans in answer:
    print(ans)