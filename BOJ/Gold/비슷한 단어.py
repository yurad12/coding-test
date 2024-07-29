# https://www.acmicpc.net/problem/2179

import sys
input = sys.stdin.readline

## O(N^2), PyPy3
N = int(input())
words = list(input().strip() for _ in range(N))

S, T = '', ''
count = 0
for i in range(N):
    word1 = words[i]
    for j in range(i+1, N):
        word2 = words[j]

        idx = 0
        n = min(len(word1), len(word2))
        while idx < n:
            if word1[idx] != word2[idx]:
                break
            idx += 1

        if count < idx:
            count = idx
            S, T = word1, word2

print(S)
print(T)


## O(NlogN), Python3
N = int(input())
input_words = list(input().strip() for _ in range(N))
words = sorted(enumerate(input_words), key = lambda x:x[1])

counts = [0] * (N+1)
count = 0
for i in range(N-1):
    idx = 0
    word1, word2 = words[i][1], words[i+1][1]
    n = min(len(word1), len(word2))
    while idx < n:
        if word1[idx] != word2[idx]:
            break
        idx += 1

    count = max(count, idx)
    counts[words[i][0]] = max(counts[words[i][0]], idx)
    counts[words[i+1][0]] = max(counts[words[i+1][0]], idx)

S, T = '', ''
max_count = max(counts)
for i in range(N):
    if not S:
        if counts[i] == max_count:
            S = input_words[i]
            prev = S[:max_count]
    else:
        if counts[i] == max_count and input_words[i][:max_count] == prev:
            T = input_words[i]
            break

print(S)
print(T)

    