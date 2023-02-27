# https://school.programmers.co.kr/learn/courses/30/lessons/42891

from heapq import heappush, heappop

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = []
    length = len(food_times)
    for i in range(length):
        heappush(q,(food_times[i],i+1))
    
    prev = 0
    while q:
        temp = length * (q[0][0] - prev)
        if temp <= k:
            k -= temp
            length -= 1
            prev, _ = heappop(q)
        else:
            # k 시간이 남아 있을 수 있으니까
            idx = k % length
            result = sorted(q, key=lambda x: x[1])
            answer = result[idx][1]
            break
                
    return answer

print(solution([3,1,2],5))
print(solution([3,1,2,5,1,3],7))