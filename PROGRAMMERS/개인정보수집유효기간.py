# https://school.programmers.co.kr/learn/courses/30/lessons/150370
# 년, 월, 일로 비교

def solution(today, terms, privacies):
    answer = []
    
    # term 사용하기 좋게 변경
    term = {}
    for i in range(len(terms)):
        a = terms[i][0]
        b = int(terms[i][1:])
        term[a] = b
    # print(term)
    
    for i in range(len(privacies)):
        privacy = privacies[i]
        year = int(privacy[:4])
        month = int(privacy[5:7])
        day = int(privacy[8:10])
        p_type = privacy[-1]
        
        # 약관에 따른 유효기간 계산
        month += term[p_type]
        if month > 12:
            year += (month//12)
            month %= 12
        day -= 1
        if day <= 0:
            day = 28
            month -= 1
        if month == 0:
            month = 12
            year -= 1
        # print(year,month,day)
        # 오늘과 유효기간 비교
        if int(today[:4]) > year:
            answer.append(i+1)
        elif int(today[:4]) >= year and int(today[5:7]) > month:
            answer.append(i+1)
        elif int(today[:4]) >= year and int(today[5:7]) >= month and int(today[8:10]) > day:
            answer.append(i+1)
        # print(answer)
    return answer