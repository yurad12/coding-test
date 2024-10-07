# https://www.acmicpc.net/problem/20310
'''
1. 앞쪽의 1은 최대한 지우기
2. 뒤쪽의 0 최대한 지우기
-> 앞쪽에는 0이 남고 뒤쪽은 1이 남음
'''

import sys
input = sys.stdin.readline

string = list(input().rstrip())

zero = string.count('0')
one = string.count('1')
answer = string

# remove 1
cnt = 0
for s in string:
    if cnt == one // 2:
        break
    if s == '1':
        answer.remove(s)
        cnt += 1

# remove 0
cnt = 0
answer = answer[::-1]
for s in string:
    if cnt == zero // 2:
        break
    if s == '0':
        answer.remove(s)
        cnt += 1

print(''.join(answer[::-1]))
