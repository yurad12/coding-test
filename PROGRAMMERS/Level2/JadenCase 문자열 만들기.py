# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = list(s)
    flag = True
    for i in range(len(answer)):
        if answer[i] == ' ':
            flag = True
            continue
        if answer[i].isdigit():
            flag = False
            continue
        if isinstance(answer[i], str):
            if flag==True:
                answer[i] = answer[i].upper()
                flag = False
            else:
                answer[i] = answer[i].lower()
    answer = ''.join(answer)
    return answer