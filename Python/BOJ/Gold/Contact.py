# https://www.acmicpc.net/problem/1013
import sys
input = sys.stdin.readline
import re

pattern = re.compile('(100+1+|01)+')

T = int(input())
for _ in range(T):
    string = input().strip()
    if pattern.fullmatch(string):
        print("YES")
    else:
        print("NO")
