# https://school.programmers.co.kr/learn/courses/30/lessons/17677

import math

def solution(str1, str2):
    answer = 0
    
    if not str1 and not str2:
        return 65536
    
    list1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    list2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    
    intersect, union = [], list2[:]
    for ch1 in list1:
        if ch1 in list2:
            intersect.append(ch1)
            list2.remove(ch1)
        else:
            union.append(ch1)
    
    if not union:
        answer = 65536
    else:
        answer = math.floor((len(intersect) / len(union)) * 65536)
        
    return answer