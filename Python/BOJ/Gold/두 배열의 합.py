# https://www.acmicpc.net/problem/2143
# prefix_A, prefix_B 반복문 -> Counter 맵 사용
import sys
input = sys.stdin.readline
from collections import Counter

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

def make_prefix_sum(arr, size):
    prefix_sum = []
    for i in range(size):
        cur_sum = 0
        for j in range(i, size):
            cur_sum += arr[j]
            prefix_sum.append(cur_sum)
    
    return prefix_sum

prefix_A = make_prefix_sum(A, n)
prefix_B = make_prefix_sum(B, m)

count_B = Counter(prefix_B)
answer = 0
for a in prefix_A:
    answer += count_B[T-a]

print(answer)