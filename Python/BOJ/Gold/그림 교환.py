# https://www.acmicpc.net/problem/1029
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
board = [list(map(int, input().strip())) for _ in range(N)]
answer = 1
visited = {}

def sell(seller, price, now):
    global answer

    state = (seller, price, frozenset(now))
    if state in visited:
        return        

    if len(now) > answer:
        answer = len(now)
    
    for buyer in range(N):
        if buyer in now or buyer == seller:
            continue

        if board[seller][buyer] >= price:
            sell(buyer, board[seller][buyer], now|{buyer})
    
    visited[state] = answer

sell(0, 0, {0})
print(answer)
