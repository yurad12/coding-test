# https://www.acmicpc.net/problem/10825
import sys
n = int(sys.stdin.readline())
score = []
for i in range(n):
    data = sys.stdin.readline().split()
    score.append((data[0], int(data[1]), int(data[2]), int(data[3])))

score = sorted(score, key = lambda x: (-x[1],x[2],-x[3],x[0]))
for s in score:
    print(s[0])