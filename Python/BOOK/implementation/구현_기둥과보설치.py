# https://www.programmers.co.kr/learn/courses/30/lessons/60061

def check(answer):
    for ans in answer:
        x, y, a = ans
        if a == 0:
            # 아래 기둥 있는지, 바닥인지, 보의 끝인지, 밑에 보가 있는지
            if [x,y-1,0] in answer or y == 0 or [x,y,1] in answer or [x-1,y,1] in answer:
                continue
            return False
        
        elif a == 1:
            # 아래에 기둥 있는지, 양쪽에 보가 있는지, 오른쪽 아래에 기둥있는지
            if [x,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer) or [x+1,y-1,0] in answer:
                continue
            return False
    return True
    
def solution(n, build_frame):
    answer = []
    for build in build_frame:
        x, y, a, b = build
        if b == 1:
            answer.append([x,y,a])
            if not check(answer): answer.remove([x,y,a])
        elif b == 0:
            answer.remove([x,y,a])
            if not check(answer): answer.append([x,y,a])
                
    answer = sorted(answer) # x좌표 기준 오름차순, 같으면 y좌표 기준 오름차순 정렬됨
    return answer