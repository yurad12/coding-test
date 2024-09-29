# https://school.programmers.co.kr/learn/courses/30/lessons/64062

def solution(stones, k):
    answer = 0
    left, right = 1, max(stones)
    
    while left <= right:
        mid = (left+right) // 2
        cnt = 0 # stones 원소에서 mid 뻈을 때, 0이 나오는 횟수
        for stone in stones:
            if (stone-mid) <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt < k:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1
            
    return answer