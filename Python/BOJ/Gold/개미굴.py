# https://www.acmicpc.net/problem/14725

import sys
input = sys.stdin.readline

N = int(input())
tree = {}
for _ in range(N):
    path = list(map(str.strip, input().split()))
    K, path = int(path[0]), path[1:]
    node = tree
    for s in path:
        if s not in node:
            node[s] = {}
        node = node[s]

stack = []
keys = sorted(tree.keys(), reverse = True)
for key in keys:
    stack.append((key, tree[key], 0))

while stack:
    key, node, depth = stack.pop()
    print('--' * depth + key)
    for key in sorted(node.keys(), reverse=True):
        stack.append((key, node[key], depth+1))

