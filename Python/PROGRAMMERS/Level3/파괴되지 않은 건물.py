# https://school.programmers.co.kr/learn/courses/30/lessons/92344?language=python3

def solution(board, skill):
    m, n = len(board), len(board[0])
    durability = [[0] * (n+1) for _ in range(m+1)]
    
    for t, r1, c1, r2, c2, d in skill:
        if t == 1:
            d = -d
        
        durability[r1][c1] += d
        durability[r1][c2+1] += -d
        durability[r2+1][c1] += -d
        durability[r2+1][c2+1] += d
    
    for i in range(1, m+1):
        for j in range(n+1):
            durability[i][j] += durability[i-1][j]
    
    for j in range(1, n+1):
        for i in range(m+1):
            durability[i][j] += durability[i][j-1]
    
    for i in range(m):
        for j in range(n):
            board[i][j] += durability[i][j]
    
    answer = len([1 for i in range(m) for j in range(n) if board[i][j] > 0])
    
    return answer