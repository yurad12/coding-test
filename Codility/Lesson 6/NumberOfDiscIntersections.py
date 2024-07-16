'''
https://app.codility.com/programmers/lessons/6-sorting/number_of_disc_intersections/
1. 시작점과 끝점 배열 생성
    - start_points[i]는 원의 시작점 (중심 - 반지름)
    - end_points[i]는 원의 끝점 (중심 + 반지름)
2. 시작점과 끝점 정렬
    - start_points와 end_points를 각각 오름차순으로 정렬
3. 교차 횟수 계산
    - start_points를 순회하면서 현재 활성화된 원의 수 추적
    - start_points[j]가 end_points[i]보다 작거나 같은 경우, 활성화된 원의 수를 증가
    - 현재 활성화된 원의 수에서 하나를 빼고, 교차 횟수를 계산
'''

def solution(A):
    n = len(A)
    start = [0] * n
    end = [0] * n
    for i in range(n):
        start[i] = i - A[i]
        end[i] = i + A[i]
    
    start.sort()
    end.sort()

    answer = 0
    disc = 0
    j = 0
    for i in range(n):
        while j < n and end[i] >= start[j]:
            disc += 1
            j += 1
        disc -= 1
        answer += disc
        if answer > 10_000_000:
            return -1
    
    return answer