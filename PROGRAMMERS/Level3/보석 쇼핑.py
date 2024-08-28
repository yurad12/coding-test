# https://school.programmers.co.kr/learn/courses/30/lessons/67258

def solution(gems):
    answer = [0, len(gems)-1]
    n = len(set(gems))
    
    start, end = 0, 0
    window = {}
    
    while end < len(gems):
        if gems[end] in window:
            window[gems[end]] += 1
        else:
            window[gems[end]] = 1
        
        # 모든 보석을 다 모은 경우
        while len(window) == n:
            if (end-start) < (answer[1]-answer[0]):
                answer = [start, end]
            
            # start 포인터를 한 칸 이동시키기 전에 현재 start가 가리키는 보석의 개수를 줄임
            window[gems[start]] -= 1
            if not window[gems[start]]:
                del window[gems[start]]
            start += 1
            
        end += 1
    
    answer = [answer[0]+1, answer[1]+1]
    return answer