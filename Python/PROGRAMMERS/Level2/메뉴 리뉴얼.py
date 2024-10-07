# https://school.programmers.co.kr/learn/courses/30/lessons/72411

# sol1
from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    dishes = defaultdict(int)
    
    for o in orders:
        order = list(o)
        order.sort()
        for c in course:
            if len(order) < c:
                break
            comb = list(combinations(order, c))
            for dish in comb:
                dishes[dish] += 1
    sorted_dishes = sorted(dishes.items(), key = lambda x: (len(x[0]), -x[1]))
    
    answer = []
    now = [0, 0] # 길이, 개수
    for dish, cnt in sorted_dishes:
        if cnt < 2:
            continue
        if len(dish) != now[0]:
            now[0], now[1] = len(dish), cnt
            answer.append(''.join(dish))
            continue
        if cnt == now[1]:
            answer.append(''.join(dish))
    
    answer.sort()
    return answer

# sol2
from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []
    
    for c in course:
        dish_count = defaultdict(int)
        
        for order in orders:
            order = sorted(order)
            combs = combinations(order, c)
            for comb in combs:
                dish_count[comb] += 1
        
        if not dish_count:
            continue
        max_count = max(dish_count.values())
        if max_count > 1:
            for dish, cnt in dish_count.items():
                if max_count == cnt:
                    answer.append(''.join(dish))
    answer.sort()
    return answer