'''
https://school.programmers.co.kr/learn/courses/30/lessons/64064

1. user_id:banned_id = n:n
banned_id 수에 따라 user_id로 만들 수 있는 순열 expected_list를 구한다.
2. banned_id 내 각각의 원소에 매치되는 후보를 순열 expected_list에서 구한다.
순열은 순서만 바뀌기 때문에 중복될 수 있다. 
ex) user_id = (’frodo’, ‘fradi’); banned_id = (’fr*d*’, ‘fr*d*’); expected_list = [(’frodo’, ‘fradi’), (’fradi’, ‘frodo’)]
set으로 바꾸고, result 리스트에 존재하는 지 확인한다.
존재하지 않으면, result 리스트에 추가한다.
3. 1, 2번의 과정을 통해 구해진 result의 길이가 나올 수 있는 제재 아이디 목록 수이다.
'''

from itertools import permutations

def check_user(users, banned_users):
    for i in range(len(users)):
        if len(users[i]) != len(banned_users[i]):
            return False
        for j in range(len(users[i])):
            if users[i][j] != banned_users[i][j] and banned_users[i][j] != "*":
                return False
    return True

def solution(user_id, banned_id):
    result = []
    expected_list = list(permutations(user_id, len(banned_id)))
    
    for users in expected_list:
        if check_user(users, banned_id) and set(users) not in result:
            result.append(set(users))
                
        
    return len(result)