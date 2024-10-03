# https://school.programmers.co.kr/learn/courses/30/lessons/42890

from itertools import combinations

def solution(relation):
    r, c = len(relation), len(relation[0])
    
    result = []
    for i in range(1, c+1):
        for combs in combinations(range(c),i):
            candidates = set()
            for rel in relation:
                now = tuple(rel[comb] for comb in combs)
                candidates.add(now)
                
            if len(candidates) == r:
                result.append(set(combs))
    
    keys = []
    for key1 in result:
        is_minimal = True
        for key2 in keys:
            if set(key2).issubset(set(key1)):
                is_minimal = False
                break
                
        if is_minimal:
            keys.append(key1)

    answer = len(keys)
    
    return answer