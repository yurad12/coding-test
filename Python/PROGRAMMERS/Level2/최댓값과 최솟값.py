# https://school.programmers.co.kr/learn/courses/30/lessons/12939?language=python3

def solution(s):
    nums = list(map(int, s.split(' ')))
    answer = ' '.join([str(min(nums)), str(max(nums))])
    return answer