# https://school.programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    answer = []
    modified_s = s.replace("{{", "[[").replace("}}", "]]").replace("},{", "],[")
    list_s = eval(modified_s)
    list_s.sort(key=len)
    
    for sub_list in list_s:
        for num in sub_list:
            if num not in answer:
                answer.append(num)
    
    return answer