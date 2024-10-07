# https://school.programmers.co.kr/learn/courses/30/lessons/118667

# solution1
from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum_q1 = sum(q1)
    sum_q2 = sum(q2)
    target = (sum_q1 + sum_q2) / 2

    for _ in range(len(queue1)*4):
        if sum_q1 == sum_q2:
            return answer
        elif sum_q1 > sum_q2:
            num = q1.popleft()
            q2.append(num)
            sum_q1 -= num
            sum_q2 += num
        else:
            num = q2.popleft()
            q1.append(num)
            sum_q2 -= num
            sum_q1 += num
        answer += 1
    return -1

# solution2
def solution(que1, que2):
    queSum = (sum(que1) + sum(que2))
    target = queSum // 2

    n = len(que1)
    start = 0
    end = n - 1
    ans = 0

    cur = sum(que1)
    que3 = que1 + que2
    while cur != target:
        if cur < target:
            end += 1
            if end == n * 2:
                return -1
            cur += que3[end]
        else:
            cur -= que3[start]
            start += 1
        ans += 1
    return ans