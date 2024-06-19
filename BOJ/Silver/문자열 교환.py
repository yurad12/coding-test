# https://www.acmicpc.net/problem/1522
'''
문자 위치 바꾸기 -> 투포인터?
슬라이싱하면서 왼쪽의 슬라이싱 내 b와 오른쪽의 슬라이싱 밖 a와 바꾸기
원형리스트라서 a개수만큼 문자열 s에 붙여주기
-> 슬라이싱 범위를 a개수로 하고, 그 안의 b 개수가 가장 적을 때가 answer
'''

import sys
input = sys.stdin.readline

s = list(input().strip())
count = s.count('a')
answer = int(1e9)

s += s[0:count-1]
for i in range(len(s)-(count-1)):
    answer = min(answer, s[i:i+count].count('b'))

print(answer)
    
