'''
https://school.programmers.co.kr/learn/courses/30/lessons/42747

https://en.wikipedia.org/wiki/H-index
'''

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for citation in citations:
        if citation > answer:
            answer += 1
    return answer
