# https://school.programmers.co.kr/learn/courses/30/lessons/17680
# [a,b,c]에서 b -> [a,c,b]

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque([], maxlen=cacheSize)
    
    for city in cities:
        c = city.lower()
        if c in cache:
            cache.remove(c)
            answer += 1
        else:
            answer += 5
        cache.append(c)
            
    return answer