# https://www.acmicpc.net/problem/22251
# n: 층수, k: LED 크기, p: 최대 변경 횟수, x: 현재 층

import sys
input = sys.stdin.readline

n, k, p, x = map(int, input().split())
nums = ['1111101', '0000101', '1011011', '1001111', '0100111',
        '1101110', '1111110', '1000101', '1111111', '1101111']

x = str(x).zfill(k)
bit_x = [nums[int(i)] for i in x]

def is_possible(x, floor):
    count = 0
    for a, b in zip(bit_x, bit_floor):
        for bit_a, bit_b in zip(a,b):
            if bit_a != bit_b:
                count += 1
        if count > p:
            return False
    if count < 1:
        return False
    return True

answer = 0
for i in range(1,n+1):
    floor = str(i).zfill(k)
    bit_floor = [nums[int(f)] for f in floor]

    if is_possible(bit_x,bit_floor):
        answer += 1

print(answer)
