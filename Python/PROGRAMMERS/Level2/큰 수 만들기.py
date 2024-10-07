# 
'''
스택 이용
전체 number 탐색 -> 스택에 넣은 마지막값이 num보다 작으면 다 빼기
'''

def solution(number, k):
    answer = [0]
    k += 1
    for i in range(len(number)):
        num = int(number[i])
        while answer and k and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
    answer = answer[:-k] if k > 0 else answer
    return ''.join(map(str, answer))