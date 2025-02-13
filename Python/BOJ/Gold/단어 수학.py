# https://www.acmicpc.net/problem/1339
import sys
input = sys.stdin.readline

N = int(input())
words = [list(input().strip()) for _ in range(N)]

words_dict = {}
for word in words:
    i = len(word) - 1
    for ch in word:
        if ch not in words_dict:
            words_dict[ch] = 10 ** i
        else:
            words_dict[ch] += 10 ** i
        i -= 1

sorted_words = sorted(words_dict.values(), reverse = True)
answer = 0
now = 9
for num in sorted_words:
    answer += num * now
    now -= 1

print(answer)