# https://www.acmicpc.net/problem/1043
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
secrets = list(map(int, input().split()))[1:]
parties = [list(map(int, input().split()))[1:] for _ in range(M)]

parent = [i for i in range(N+1)]
for party in parties:
    for i in range(1,len(party)):
        union_parent(parent, party[0], party[i])

truth_group = set()
for p in secrets:
    truth_group.add(find_parent(parent, p))

answer = 0
party = [False] * (M+1)
for party in parties:
    flag = True
    for p in party:
        if find_parent(parent, p) in truth_group:
            flag = False
            break
    if flag:
        answer += 1

print(answer)
