# https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 4, reverse=True)
    answer = ''.join(numbers)
    if answer[0] == '0':
        return '0'
    return answer
