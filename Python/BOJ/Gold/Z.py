# https://www.acmicpc.net/problem/1074
import sys
input = sys.stdin.readline

def find(x, y, n):
    global answer
    d = [(0,0), (0,1), (1,0), (1,1)]

    if x > r or x+n <= r or y > c or y+n <= c:
        answer += n ** 2
        return
    
    if n >= 2:
        n //= 2
        find(x, y, n)
        find(x, y+n, n)
        find(x+n, y, n)
        find(x+n, y+n, n)
    else:
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            if nx == r and ny == c:
                print(answer + i)
                sys.exit()

N, r, c = map(int, input().split())
answer = 0
find(0,0,2 ** N)
