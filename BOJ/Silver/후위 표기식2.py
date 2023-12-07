# https://acmicpc.net/problem/1935

'''
123*+45/-
(6+1)-4/5 = 31/5 = 6.2
'''

import sys
input = sys.stdin.readline

n = int(input())
func = input()
nums = dict()
for f in func:
    if f.isalpha() and f not in nums:
        num = int(input())
        nums[f] = num

q = []
calc = 0
for f in func:
    if f.isalpha():
        q.append(nums[f])
        continue
    else:
        if len(q) == 1:
            break
        a = q.pop()
        b = q.pop()
    
    if f == "*":
        calc =  b * a
    elif f == "+":
        calc = b + a
    elif f == "/":
        calc = b / a
    elif f == "-":
        calc = b - a
    
    q.append(calc)

print("{:.2f}".format(q[0]))