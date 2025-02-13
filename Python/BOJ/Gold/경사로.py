# https://www.acmicpc.net/problem/14890
import sys
input = sys.stdin.readline

N, L =  map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def place(road):
    slope = [0] * N

    for i in range(N-1):
        if abs(road[i] - road[i+1]) > 1:
            return False
        
        if road[i] - road[i+1] == 1: # 높->낮
            for j in range(i+1, i+1+L):
                if j >= N or road[i+1] != road[j] or slope[j]:
                    return False
                if not slope[j]:
                    slope[j] = 1
        elif road[i] - road[i+1] == -1: # 낮->높
            for j in range(i+1-L, i+1):
                if j < 0 or road[i] != road[j] or slope[j]:
                    return False
                if not slope[j]:
                    slope[j] = 1

    return True


answer = 0
for i in range(N):
    if place(board[i]):
        answer += 1
for j in range(N):
    road = [board[i][j] for i in range(N)]
    if place(road):
        answer += 1

print(answer)
