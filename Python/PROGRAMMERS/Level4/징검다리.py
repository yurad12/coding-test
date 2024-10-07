# https://school.programmers.co.kr/learn/courses/30/lessons/43236

'''
풀이
1. 이분탐색할 값의 기준: 바위 거리
 - 바위 거리를 계산해서 최소 중에 최대를 구한다.
2. 모든 바위를 탐색하면서 바위 거리가 최소일 때 제거할 수 있는 바위 수를 구한다.
 - 바위 거리: rocks[i] - prev_rock
 - 바위 거리가 mid값보다 작다는 것은 해당 바위를 제거할 수 있다는 의미
 - 바위 거리가 mid값보다 크다는 것은 해당 바위를 제거할 수 없으므로 현재 바위로 위치를 옮긴다.
 3. 제거한 바위 수와 실제 제거해야하는 바위 수를 비교한다.
 - removed_rocks가 n보다 크다는 것은 제거할 수 있는 바위가 많기 때문에 end를 줄여서 다시 탐색
 - removed_rocks가 n보다 작다는 것은 제거할 수 있는 바위의 최대이기 때문에 answer에 해당 값을 넣고 start를 늘려서 다시 탐색
'''

def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    
    length = len(rocks)
    start, end = 0, distance
    
    while start <= end:
        mid = (start + end) // 2
        prev_rock = 0
        removed_rocks = 0
        
        for i in range(length):
            if rocks[i] - prev_rock < mid:
                removed_rocks += 1
            else:
                prev_rock = rocks[i]
        if distance - prev_rock < mid:
            removed_rocks += 1
        
        if removed_rocks > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    
    return answer