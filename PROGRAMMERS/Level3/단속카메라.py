'''
차량의 진입/진출 시점에 카메라를 설치함
1. 진출 시점을 기준으로 오름차순 정렬
2. 다음 차량 진입시점 <= 진출시점 <= 다음 차량 진출 시점, continue
 아니면, 진출시점을 다음 차량의 진출시점으로 변경, answer += 1
'''

def solution(routes):
    answer = 0
    routes.sort(key = lambda x: x[1])
    camera = -30_001
    
    for a, b in routes:
        if a <= camera <= b:
            continue
        camera = b
        answer += 1
    return answer