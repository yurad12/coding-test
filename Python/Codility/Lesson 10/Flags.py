'''
https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/flags/

- 시간복잡도: O(N)
'''

def solution(A):
    peaks = []
    for i in range(1,len(A)-1):
        if A[i-1] < A[i] and A[i] > A[i+1]:
            peaks.append(i)
    
    if not peaks:
        return 0

    if len(peaks) < 3:
        return len(peaks)

    def place(k):
        last = peaks[0]
        count = 1
        for i in range(1,len(peaks)):
            if peaks[i]-last >= k:
                count += 1
                last = peaks[i]
            if count == k:
                return True
        return False
    
    answer = 0
    start, end = 1, len(peaks)
    while start <= end:
        mid = (start + end) // 2
        if place(mid):
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
    
    return answer