# https://www.acmicpc.net/problem/14889
import sys
input = sys.stdin.readline

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

def get_diff(team):
    A = list(team)
    B = list(set(range(N)) - team)
    sum_a = 0
    sum_b = 0

    for i in range(len(A)):
        for j in range(i+1, len(A)):
            sum_a += (points[A[i]][A[j]] + points[A[j]][A[i]])
    
    for i in range(len(B)):
        for j in range(i+1, len(B)):
            sum_b += (points[B[i]][B[j]] + points[B[j]][B[i]])

    return abs(sum_a - sum_b)

def dfs(team, idx):
    global answer
    if len(team) == N // 2:
        answer = min(answer, get_diff(team))
        return
    
    for i in range(idx, N):
        if i not in team:
            dfs(team | {i}, i + 1)

answer = float('inf')
dfs(set(), 0)
print(answer)