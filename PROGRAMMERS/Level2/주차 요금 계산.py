# https://school.programmers.co.kr/learn/courses/30/lessons/92341

import math

def solution(fees, records):    
    # key: 차 번호, value: [[시간], 현재 상태] -> 시간 in 이면 append, out이면 계산
    lot = {}
    
    for record in records:
        time, number, status = record.split(' ')
        if number not in lot:
            lot[number] = [[], 0]

        if status == 'IN':
            lot[number][0].append(time)
            lot[number][1] = 1
        else:
            sh, sm = lot[number][0][-1].split(':')
            eh, em = time.split(':')
            lot[number][0][-1] = (int(eh) - int(sh)) * 60 + int(em) - int(sm)
            lot[number][1] = 0

    answer = []
    for key, values in lot.items():
        if values[1]:
            sh, sm = values[0][-1].split(':')
            lot[key][0][-1] = (23 - int(sh)) * 60 + 59 - int(sm)
            lot[key][1] = 0
        
        cost = fees[1]
        total = sum(lot[key][0])
        if total > fees[0]:
            cost += math.ceil((total - fees[0]) / fees[2]) * fees[3]
        lot[key].append(cost)
    
    sorted_lot = sorted(lot.items(), key = lambda x: x[0])
    answer = [i[-1][-1] for i in sorted_lot]
    
    return answer