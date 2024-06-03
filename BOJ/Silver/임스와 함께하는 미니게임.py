# https://www.acmicpc.net/problem/25757

import sys
input = sys.stdin.readline

n, g = input().split()
games = {'Y':2, 'F':3, 'O':4}

people = set()
for _ in range(int(n)):
    name = input().strip()
    people.add(name)

print(len(people) // (games[g]-1))