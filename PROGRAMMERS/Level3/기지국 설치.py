'''
https://school.programmers.co.kr/learn/courses/30/lessons/12979#

1. 자기 자신과 좌, 우로 전달되므로 range = w * 2 + 1
2. 기지국이 설치되지 않는 거리 dist = station - w - start
3. start는 기지국이 설치된 마지막 위치 + 1
4. 1-3 반복
'''

def solution(n, stations, w):
    answer = 0

    start = 1
    for station in stations:
        dist = station - w - start
        if dist > 0:
            answer += dist // (2*w+1)
            answer += (1 if dist % (2*w+1) > 0 else 0)
        start = station + w + 1
    if start <= n:
        dist = n-start+1
        answer += dist // (2*w+1)
        answer += (1 if dist % (2*w+1) > 0 else 0)
    
    return answer