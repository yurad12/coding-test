# https://www.acmicpc.net/problem/9655

import sys
input = sys.stdin.readline

n = int(input())

if n % 2:
    print("SK")
else:
    print("CY")