# https://school.programmers.co.kr/learn/courses/30/lessons/12924

### solution1
def solution(n):
    answer = 0
    for i in range(1, n+1):
        current_value = i
        sum_value = i
        while sum_value <= n:
            if sum_value == n:
                answer += 1
                break
            current_value += 1
            sum_value += current_value
    return answer


### solution2: 등차수열 합 이용
def solution(n):
    answer = len([i  for i in range(1,num+1,2) if num % i is 0])
    return answer