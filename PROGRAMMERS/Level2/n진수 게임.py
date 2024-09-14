# https://school.programmers.co.kr/learn/courses/30/lessons/17687?language=python3#

def solution(n, t, m, p):
    
    def convert(n, i):
        S = '0123456789ABCDEF'
        converted = ''
        while i > 0:
            converted = S[i%n] + converted
            i //= n
        return converted

    nums = '0'
    for i in range(t*m):
        nums += convert(n, i)
    
    answer = ''
    for i in range(p-1, t*m, m):
        answer += nums[i]
        
    return answer