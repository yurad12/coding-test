# https://www.acmicpc.net/problem/16162
import sys
input = sys.stdin.readline

N, A, D = map(int, input().split())
tones = list(map(int, input().split()))

answer = 0
for i in range(N):
    if tones[i] < A:
        continue

    if (tones[i] - A) % D == 0:
        tone = (tones[i] - A) // D + 1
        if tone - answer == 1:
            answer += 1

print(answer)