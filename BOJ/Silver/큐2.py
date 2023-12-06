# https://www.acmicpc.net/problem/18258

# solution1: 메모리(382012kb), 시간(2432ms)
import sys
input = sys.stdin.readline

n = int(input())
commands = []
for _ in range(n):
    action = input().rstrip()
    if action[:4] == "push":
        commands.append((action[:4], int(action[4:])))
    else:
        commands.append(action)

start = 0
end = 0
q = []
for command in commands:
    if len(command) > 1 and command[0] == "push":
        q.append(command[1])
        end += 1
    elif command == "pop":
        if start >= end:
            print(-1)
        else:
            print(q[start])
            start += 1
    elif command == "front":
        if start >= end:
            print(-1)
        else:
            print(q[start])
    elif command == "back":
        if start >= end:
            print(-1)
        else:
            print(q[end-1])
    elif command == "size":
        print(end-start)
    elif command == "empty":
        if start >= end:
            print(1)
        else:
            print(0)
    elif command == "size":
        if start >= end:
            print(0)
        else:
            print(end-start)


# solution2: 메모리(175180kb), 시간(1504ms)
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
q = deque()
for _ in range(n):
    command = input().split()
    print(command)
    if command[0] == "push":
        q.append(command[1])
    elif command[0] == "pop":
        print(q.popleft() if q else -1)
    elif command[0] == "size":
        print(len(q))
    elif command[0] == "empty":
        print(1 if not q else 0)
    elif command[0] == "front":
        print(q[0] if q else -1)
    elif command[0] == "back":
        print(q[-1] if q else -1)
    