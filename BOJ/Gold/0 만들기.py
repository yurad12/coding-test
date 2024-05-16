import sys
input = sys.stdin.readline

case = int(input())

def dfs(res, op, num, idx, string):
    if idx == n:
        res += (op * num)
        if res == 0:
            print(string)
    else:
        dfs(res, op, num*10+(idx+1), idx+1, string+' '+str(idx+1))
        dfs(res+op*num, 1, idx+1, idx+1, string+'+'+str(idx+1))
        dfs(res+op*num, -1, idx+1, idx+1, string+'-'+str(idx+1))

for _ in range(case):
    n = int(input())
    dfs(0,1,1,1,"1")
    print()


'''
1-2 3-4 5+67
 -> 1, -
 -> 1, - 23
 -> -22, -
 -> -22, - 45
 -> -67, +
 -> -67, + 67 = 0

1. dfs로 사용할 것
 - res: 지금까지 결과
 - op: 현재 연산자
 - num: 현재 숫자
 - idx: 현재 인덱스
 - string: 현재 수식 문자열
2. dfs 3가지 수행
 - 덧셈
 - 뺄셈
 - 숫자 붙이기
'''