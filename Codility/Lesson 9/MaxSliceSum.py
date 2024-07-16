'''
https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_slice_sum/

- 카데인(Kadane) 알고리즘 이용
- 자기 자신과 자기자신+이전 중 최댓값을 갱신하는 방식
'''

def solution(A):
    dp = [0] * len(A)
    dp[0] = A[0]
    for i in range(1,len(A)):
        dp[i] = max(A[i], dp[i-1]+A[i])

    return max(dp)