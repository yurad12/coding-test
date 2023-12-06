# https://school.programmers.co.kr/learn/courses/30/lessons/81302

def solution(places):
    answer = []
    
    # 상하좌우, 2칸
    dx1 = [-1,1,0,0]
    dy1 = [0,0,-1,1]
    # 대각선
    dx2 = [-1,-1,1,1]
    dy2 = [-1,1,-1,1]
    
    for place in places:
        result = 1
        for x in range(5):
            for y in range(5):
                if not result:
                    break
                if place[x][y] != 'P':
                    continue
                    
                # 상하좌우
                for i in range(4):
                    nx = x + dx1[i]
                    ny = y + dy1[i]
                    if 0<=nx<5 and 0<=ny<5 and place[nx][ny] == 'P':
                        # print("상하좌우", place[nx][ny])
                        result = 0
                        break
                # 대각선
                for i in range(4):
                    nx = x + dx2[i]
                    ny = y + dy2[i]
                    if 0<=nx<5 and 0<=ny<5 and place[nx][ny] == 'P':
                        if place[x][ny] != 'X' or place[nx][y] != 'X':
                            result = 0
                            # print("대각선", place[x][ny], place[nx][y])
                            break
                # 2칸
                for i in range(4):
                    nx = x + dx1[i]*2
                    ny = y + dy1[i]*2
                    if 0<=nx<5 and 0<=ny<5 and place[nx][ny] == 'P':
                        if place[x+dx1[i]][y+dy1[i]] != 'X':
                            result = 0
                            # print("2칸", place[x+dx1[i]][y+dy1[i]])
                            break
    
        answer.append(result)
        
    return answer