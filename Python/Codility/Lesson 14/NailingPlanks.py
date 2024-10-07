# https://app.codility.com/programmers/lessons/14-binary_search_algorithm/nailing_planks/
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, C):

    def check_planks(A, B, C, mid):
        N = len(A)
        nails = C[:mid+1]
        nails.sort()

        for k in range(N):
            left, right = A[k], B[k]
            start, end = 0, len(nails)-1
            fixed = False
            
            while start <= end:
                mid = (start + end) // 2
                if left <= nails[mid] <= right:
                    fixed = True
                    break
                elif nails[mid] < left:
                    start = mid + 1
                else:
                    end = mid - 1
            if not fixed:
                return False
        return True
    

    start, end = 0, len(C)-1
    answer = -1

    while start <= end:
        mid = (start + end) // 2
        if check_planks(A, B, C, mid):
            end = mid - 1
            answer = mid + 1
        else:
            start = mid + 1
    
    return answer


'''
* 풀이
    1. `check_planks`: 첫 번째부터 mid까지 못 사용했을 때, 모든 판자가 고정되는지 확인
        - 이진탐색해야하니까 정렬
        2. 이진탐색으로 판자 범위 A[k], B[k] 내에 못이 있는지 확인
    2. 이진탐색으로 최소 못 개수 찾기
        - `check_planks`로 mid번째까지 못으로 모든 판자 고정할 수 있는지 확인
'''