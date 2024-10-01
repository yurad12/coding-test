# https://school.programmers.co.kr/learn/courses/30/lessons/150368
'''
1. 할인율 중복 순열 구하기
2. 할인율 중복 순열마다 이모티콘 구매 비용과 서비스 가입 여부 확인
3. 서비스 가입자 수 최대이면서 판매액도 최대한 큰 값으로 answer 갱신
'''

from itertools import product

def solution(users, emoticons):
    discount_rate = [10, 20, 30, 40]
    rate_product = list(product(discount_rate, repeat=len(emoticons)))

    answer = [0,0]
    for rate in rate_product:
        sales = 0
        subscribers = 0
        
        for user in users:
            total_price = 0
            service = False
            
            for i, em in enumerate(emoticons):
                if rate[i] >= user[0]:
                    total_price += em * (100-rate[i]) / 100
                    if total_price >= user[1]:
                        service = True
                        break
                        
            if service:
                subscribers += 1
            else:
                sales += total_price
            
        if answer[0] < subscribers:
            answer = [subscribers, sales]
        elif answer[0] == subscribers:
            if answer[1] < sales:
                answer = [subscribers, sales]
    
    return answer