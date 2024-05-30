# https://www.acmicpc.net/problem/2607
# 비슷한 단어: 같은 구성 or 한 문자 더하기 or 빼기 or 바꾸기

import sys
input = sys.stdin.readline

n = int(input())
target = input().strip()
words = list(input().strip() for _ in range(n-1))
result = 0

for i in range(n-1):
    word = list(words[i])
    count = 0
    for char in target:
        if char in word:
            word.remove(char)
        else:
            count += 1
    if count < 2 and len(word) < 2:
        result += 1

print(result)
