# https://www.acmicpc.net/problem/1011
'''
1 // 1 1 // 1 1 1 / 1 2 1 // 1 2 1 1 / 1 2 2 1 // 1 2 2 1 1
'''
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    
    total_dist = y - x
    now_dist = 0
    moves, k = 0, 0 # 이동 횟수, 광년

    while now_dist < total_dist:
        moves += 1
        if moves % 2 == 1:
            k += 1
        now_dist += k
    
    print(moves)
    