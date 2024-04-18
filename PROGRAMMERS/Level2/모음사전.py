'''
https://school.programmers.co.kr/learn/courses/30/lessons/84512

'A':0,'E':1,'I':2,'O':3,'U':4
A, AA, AAA, AAAA, AAAAA
-> AAAAE, AAAAI, AAAAO, AAAAU
-> AAAE,
-> AAE,

AAE에서 E의 위치를 찾는 다고 하면,
1. E위치에서의 경우의 수가 5^3
AAA, AAE...EAA...UUU 이러한 경우가 5^3이고 거기서 자기자신 빼주면 5^3-1
2. 여기서 E로 시작하는 Exx 빼고는 후보에서 제외되니까 4로 나눠준다.
'''

def solution(word):
    answer = 0 
    nums = {'A':0,'E':1,'I':2,'O':3,'U':4}
    for i, alp in enumerate(word):
        temp = nums[alp] * (5**(5-i)-1) // 4 + 1
        answer += temp
    return answer