# https://acmicpc.net/problem/20920

import sys
input = sys.stdin.readline

def order_by_dictionary(w):
    orders = []
    for i in range(len(w)):
        orders.append(ord(w[i]))
    return orders

n, m = map(int, input().split())
words = {}
for _ in range(n):
    w = input().strip()
    if w not in words:
        words[w] = [0,0,[]]
    words[w][0] += 1
    words[w][1] = len(w)
    words[w][2] = order_by_dictionary(w)

sorted_words = sorted(words.items(), key = lambda x: (-x[1][0],-x[1][1], x[1][2]))
sorted_words = dict(sorted_words)

for key in sorted_words.keys():
    if len(key) < m:
        continue
    print(key)
