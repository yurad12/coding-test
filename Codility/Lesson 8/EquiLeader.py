'''
- 전체 배열의 리더 → 부분 배열의 리더
    - 전체 배열의 리더 찾기
        - Boyer-Moore Voting Algorithm을 사용하여 후보를 칮기
        - 후보가 과반수를 차지하는지 확인
    - 리더 검증
        - 리더가 과반수를 차지하는 경우에만 equi 리더 계산을 진행
    - equi 리더 계산
        - 배열을 순회하면서 각 위치에서 왼쪽 부분 배열의 리더 수를 세고, 나머지 오른쪽 부분 배열의 리더 수를 계산
        - 왼쪽 부분 배열과 오른쪽 부분 배열 모두에서 리더가 과반수인 경우를 세어 equi 리더를 계산
'''

def solution(A):
    count, candidate = 0, -1
    for a in A:
        if count == 0:
            count = 1
            candidate = a
        elif a == candidate:
            count += 1
        else:
            count -= 1
    
    count, leader = 0, -1
    for a in A:
        if a == candidate:
            count += 1
    if count > len(A) // 2:
        leader = candidate
    else:
        return 0
    
    left_cnt, answer = 0, 0
    for i in range(len(A)):
        if A[i] == leader:
            left_cnt += 1
        
        left_size = i + 1
        right_size = len(A) - left_size
        right_cnt = count - left_cnt

        if left_cnt > left_size // 2 and right_cnt > right_size // 2:
            answer += 1
    return answer