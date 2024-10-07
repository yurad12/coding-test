# https://school.programmers.co.kr/learn/courses/30/lessons/43165
'''
백트래킹으로
'''

def solution(numbers, target):
    answer = 0
    def dfs(idx, current):
        nonlocal answer
        if idx == len(numbers):
            if current == target:
                answer += 1
            return
        num = numbers[idx]
        dfs(idx+1, current+num)
        dfs(idx+1, current-num)
    dfs(0, 0)
    return answer