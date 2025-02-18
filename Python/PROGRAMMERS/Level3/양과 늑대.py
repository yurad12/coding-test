# https://school.programmers.co.kr/learn/courses/30/lessons/92343

def solution(info, edges):
    def dfs(now):
        nonlocal answer
        
        if visited[now]:
            return
        
        visited[now] = 1
        sheep, wolf = 0, 0
        
        for i in range(n):
            if now & (1 << i):
                sheep += info[i]^1
                wolf += info[i]
                
        if sheep <= wolf:
            return
        
        answer = max(answer, sheep)
        
        for i in range(n):
            if not now & (1 << i):
                continue
                
            if left[i] != -1:
                dfs(now | (1 << left[i]))
            if right[i] != -1:
                dfs(now | (1 << right[i]))
        
        
    answer = 1
    visited = [0] * (1 << 17)
    n = len(info)
    left = [-1] * 18
    right = [-1] * 18
    
    for a, b in edges:
        if left[a] == -1:
            left[a] = b
        else:
            right[a] = b
    
    dfs(1 << 0)
    
    return answer