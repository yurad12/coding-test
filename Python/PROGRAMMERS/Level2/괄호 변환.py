# https://school.programmers.co.kr/learn/courses/30/lessons/60058

def solution(p):
    def check_balance(s):
        stack = []
        for ch in s:
            if ch == '(':
                stack.append('(')
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
        return not stack
    
    def split_uv(s):
        stack = []
        o, c = 0, 0
        for i, b in enumerate(s):
            if b == '(':
                o += 1
            else:
                c += 1
            if o == c:
                return s[:i+1], s[i+1:]

    def recursive(s):   
        if not s:
            return ''
        
        u, v = split_uv(s)
        if check_balance(u):
            return u + recursive(v)
        else:
            new_s = '(' + recursive(v) + ')'
            u = u[1:-1]
            u = u.replace('(','temp').replace(')','(').replace('temp',')')
            return new_s + u
    
    if not p:
        return ''
    if check_balance(p):
        return p
    answer = recursive(p)
    
    return answer