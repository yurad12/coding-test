# https://www.acmicpc.net/problem/22233

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
keywords = set([input().strip() for _ in range(n)])
blogs = [list(map(str.strip, input().split(','))) for _ in range(m)]

used = set()
result = n
for blog in blogs:
    for word in blog:
        if word not in keywords:
            continue
        if word not in used:
            used.add(word)
            result -= 1
    print(result)
