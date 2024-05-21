# https://www.acmicpc.net/problem/19941

import sys
input = sys.stdin.readline

n, k = map(int,input().split())
table = list(input().strip())

result = 0
for i in range(len(table)):
    if table[i] != 'P':
        continue

    start = max(0,i-k)
    end = min(i+k+1, n)

    for j in range(start, end):
        if table[j] == 'H':
            table[j] = ''
            result += 1
            break

print(result)