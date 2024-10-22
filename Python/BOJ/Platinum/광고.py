# https://www.acmicpc.net/problem/1305
# 패턴? 
import sys
input = sys.stdin.readline

L = int(input())
s = input().strip()

n = len(s)
pt = [0] * L
j = 0
for i in range(1, L):
    while j > 0 and s[i] != s[j]:
        j = pt[j - 1]
    if s[i] == s[j]:
        j += 1
        pt[i] = j
        
answer = L - pt[L-1]
print(answer)