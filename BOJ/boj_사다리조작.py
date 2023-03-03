# https://www.acmicpc.net/problem/15684

from sys import exit

n, m, h = map(int,input().split())
if m == 0:
    print(0)
    exit()
array = [[False]*n for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().split())
    array[a-1][b-1] = True

# 도착하는 지 체크
def check():
    for start in range(n):
        k = start # 가로선
        for j in range(h):
            if array[j][k]:
                k += 1 # 가로선 위치 이동
            elif k > 0 and array[j][k-1]:
                k -= 1 # 가로선 위치 복귀
        if k != start:
            return False
    return True

answer = 4 # 안되는 값
# 가로선 놓기
def dfs(count,x,y):
    global answer
    if check():
        answer = min(answer,count)
        return
    elif count == 3 or answer <= count:
        return
    for i in range(x,h):
        if i == x: # 행이 변경되기 전에 다음 열로 이동
            k = y
        else: # 행이 변경되면 열 처음부터 탐색
            k = 0
        for j in range(k,n-1):
            if not array[i][j] and not array[i][j+1]:
                array[i][j] = True # 가로선 놓고
                dfs(count+1,i,j+2) # 탐색 후
                array[i][j] = False # 놓았던 가로선 없애기

dfs(0,0,0)
print(answer if answer<4 else -1)