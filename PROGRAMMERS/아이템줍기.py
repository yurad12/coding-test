# https://school.programmers.co.kr/learn/courses/30/lessons/87694

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # rectangle 위치
    # (3,5)에서 (3,6)으로 못가는게 갈 수 있는 거로 판단하니까 크기 2배로 늘려야 함
    array = [[-1]*102 for _ in range(102)]
    for rect in rectangle:
        ax,ay,bx,by = map(lambda x:x*2, rect)
        for x in range(ax,bx+1):
            for y in range(ay,by+1):
                if ax<x<bx and ay<y<by:
                    array[x][y] = 0
                elif array[x][y] != 0:
                    array[x][y] = 1
    
    # 아이템 위치까지 거리 구하기
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque()
    q.append((characterX*2,characterY*2))
    distance = [[int(1e9)]*102 for _ in range(102)]
    distance[characterX*2][characterY*2] = 0
    array[characterX*2][characterY*2] = 2
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<=0 or nx>101 or ny<=0 or ny>101:
                continue
            if array[nx][ny] == 1:
                array[nx][ny] = 2
                q.append((nx,ny))
                distance[nx][ny] = min(distance[nx][ny],distance[x][y] + 1)
    answer = distance[itemX*2][itemY*2] // 2
    return answer