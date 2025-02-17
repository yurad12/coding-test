# https://www.acmicpc.net/problem/5639
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

preordered = []
while True:
    try:
        n = int(input())
        preordered.append(n)
    except:
        break


def pre_to_post(start, end):
    if start >= end:
        return
    
    mid = end
    for i in range(start+1, end):
        if preordered[i] > preordered[start]:
            mid = i
            break
    
    pre_to_post(start+1, mid)
    pre_to_post(mid, end)
    print(preordered[start])

pre_to_post(0, len(preordered))