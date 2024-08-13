# https://www.acmicpc.net/problem/1655
# min_heap: 중간보다 큰 값
# max_heap: 중간 이하 값

import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input())

min_heap = []
max_heap = []

for i in range(N):
    num = int(input())

    if len(min_heap) != len(max_heap):
        heappush(min_heap, num)
    else:
        heappush(max_heap, -num)

    if min_heap and -max_heap[0] > min_heap[0]:
        max_value = heappop(max_heap)
        min_value = heappop(min_heap)
        
        heappush(max_heap, -min_value)
        heappush(min_heap, -max_value)

    print(-max_heap[0])
