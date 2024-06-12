# https://www.acmicpc.net/problem/1406
'''
시작시 커서 맨 뒤에 위치
stack 2개 활용해서 커서를 기준으로 두 개의 스택으로 분리
- stack1: 커서 왼쪽, stack2: 커서 오른쪽 뒤집은 형태
1. L: stack1에 있는 마지막 수를 stack2로 옮김
2. D: stack2에 있는 마지막 수를 stack1로 옮김
3. B: stack1에 있는 마지막 수를 제거
4. P: stack1에 추가
'''

import sys
input = sys.stdin.readline

str1 = list(input().rstrip())
n = int(input())
str2 = []

for _ in range(n):
    data = input().rstrip()
    if data[0] == 'L':
        if str1:
            str2.append(str1.pop())
    elif data[0] == 'D':
        if str2:
            str1.append(str2.pop())
    elif data[0] == 'B':
        if str1:
            str1.pop()
    else:
        str1.append(data[2])

str1.extend(reversed(str2))
print(''.join(str1))
