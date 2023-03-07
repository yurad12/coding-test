# https://www.acmicpc.net/problem/14500

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(n)]
options = [
    [(0,0),(0,1),(0,2),(0,3)], # 1번 ㅡ
    [(0,0),(1,0),(2,0),(3,0)], 
    [(0,0),(0,1),(1,0),(1,1)], # 2번 ㅁ
    [(0,0),(1,0),(2,0),(2,1)], # 3번 |_
    [(1,0),(0,0),(0,1),(0,2)],
    [(0,0),(0,1),(0,2),(1,2)], 
    [(0,0),(0,1),(1,1),(2,1)],
    [(2,0),(2,1),(1,1),(0,1)],
    [(0,0),(1,0),(1,1),(1,2)],
    [(1,0),(1,1),(1,2),(0,2)],
    [(0,1),(0,0),(1,0),(2,0)],
    [(0,0),(1,0),(1,1),(2,1)], # 4번
    [(1,0),(1,1),(0,1),(0,2)],
    [(0,0),(0,1),(1,1),(1,2)],
    [(0,1),(1,1),(1,0),(2,0)],
    [(0,0),(0,1),(0,2),(1,1)], # 5번 ㅜ
    [(1,0),(0,1),(1,1),(2,1)],
    [(0,0),(1,0),(2,0),(1,1)],
    [(0,1),(1,0),(1,1),(1,2)]
]

result = 0
def find_value(x,y):
    global result
    for option in options:
        temp = 0
        for i in range(4):
            nx = x + option[i][0]
            ny = y + option[i][1]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                break
            temp += array[nx][ny]
        result = max(result,temp)

for i in range(n):
    for j in range(m):
        find_value(i,j)
print(result)