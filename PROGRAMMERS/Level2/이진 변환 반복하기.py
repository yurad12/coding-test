# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def get_binary(n, result):
    a = n // 2
    b = n % 2
    result.append(b)
    if a == 0:
        return result
    else:
        return get_binary(a, result)

def solution(s):
    x = list(s)
    zero_count = 0
    count = 0
    
    while True:
        c = x.count('1')
        zero_count += len(x) - c
        count += 1
        if c == 1:
            break
        
        result = get_binary(c, [])
        result.sort(reverse=True)
        x = ''.join(str(i) for i in result)
    answer = [count, zero_count]
    return answer