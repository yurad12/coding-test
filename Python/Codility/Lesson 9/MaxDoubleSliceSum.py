'''
https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_double_slice_sum/

- 부분 합 계산
    - 각 인덱스 i에서 끝나는 부분 배열의 최대 합을 저장하는 배열 max_ending_here를 계산
    - 각 인덱스 i에서 시작하는 부분 배열의 최대 합을 저장하는 배열 max_starting_here를 계산
- double slice의 최대 합 계산
    - 배열을 순회하면서 double slice의 합을 계산
    - double slice (X, Y, Z)는 X < Y < Z 이므로, 
    max_ending_here[X+1]와 max_starting_here[Z-1]을 사용하여 double slice의 합을 계산
'''

def solution(A):
    n = len(A)
    if n < 4:
        return 0

    start = [0] * n
    end = [0] * n

    for i in range(1,n-1):
        start[i] = max(0, start[i-1]+A[i])
    
    for i in range(n-2,0,-1):
        end[i] = max(0, end[i+1]+A[i])
    
    answer = 0
    for i in range(1, n-1):
        answer = max(answer, start[i-1]+end[i+1])
    
    return answer