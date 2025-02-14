# https://www.acmicpc.net/problem/1068
import sys
input = sys.stdin.readline

N = int(input())
nodes = list(map(int, input().split()))
num = int(input())

tree = [[] for _ in range(N)]
root, parent = 0, 0
for i in range(N):
    if nodes[i] == -1:
        root = i
    else:
        tree[nodes[i]].append(i)

def remove(node):
    parent = nodes[node]
    if parent != -1 and node in tree[parent]:
        tree[parent].remove(node)

    for child in tree[node]:
        remove(child)
    tree[node] = []

answer = 0
def dfs(node):
    global answer

    if not tree[node]:
        answer += 1
    else:
        for child in tree[node]:
            dfs(child)

if num == root:
    print(0)
else:
    remove(num)
    dfs(root)
    print(answer)

print(tree)
'''
1> 트리 만들기
2> 노드 삭제
3> 리프 노드 개수 세기
'''