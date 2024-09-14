# https://school.programmers.co.kr/learn/courses/30/lessons/17684
from collections import deque

def solution(msg):
    # 1번
    s_dict = {}
    for i in range(26):
        ch = chr(i+65)
        s_dict[ch] = i+1
    
    # 2,3,4번
    q = deque(msg)
    w = ''
    idx = 27
    answer = []
    
    while q:
        c = q.popleft()
        if w + c in s_dict:
            w += c
            continue
        
        answer.append(s_dict[w])
        s_dict[w+c] = idx
        w = c
        idx += 1
    answer.append(s_dict[w])
    
    return answer