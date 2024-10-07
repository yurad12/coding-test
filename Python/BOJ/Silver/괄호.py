# https://www.acmicpc.net/problem/9012

import sys
input = sys.stdin.readline

t = int(input())
strings = []
for _ in range(t):
    s = input()
    strings.append(s)

def check_vps(string):
    # (로 시작해서 )로 끝나는지 확인
    # (개수와 )개수가 같아야 함
    
    count = 0
    for i in range(len(string)):
        if string[i] == "(":
            if i == len(string)-1:
                return "NO"
            count += 1
        elif string[i] == ")":
            if count == 0:
                return "NO"
            count -= 1
    
    if count == 0:
        return "YES"
    else:
        return "NO"

for s in strings:
    print(check_vps(s))
