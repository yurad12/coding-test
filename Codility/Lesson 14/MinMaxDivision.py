# https://app.codility.com/programmers/lessons/14-binary_search_algorithm/min_max_division/
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(K, M, A):
    answer = 0

    start, end = max(A), sum(A)
    while start <= end:
        mid = (start + end) // 2

        blocks, total = 1, 0
        for a in A:
            if total + a <= mid:
                total += a
            else:
                total = a
                blocks += 1

        if blocks > K:
            start = mid + 1
        else:
            end = mid - 1
            answer = mid

    return answer
    
'''
* 풀이
1. 이진탐색으로 어떤 구간으로 나눴을 때의 최대 합을 설정
    a. start = max(A), end = sum(A)
    b. mid 값이 최댓값
2. 배열에서 mid값이 최댓값을 넘지 않게 구간을 나눴을 때, 구간이 K 구간이 되는지 확인

* 참고
    - 처음에 start값을 M으로 두었는데, 틀렸음
    - 예를들어, M = 10, [2,3,8]이면 배열의 최댓값이 M이라고 보장할 수 없음
'''