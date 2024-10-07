import sys
input = sys.stdin.readline

m = int(input())
s = set()

while m > 0:
    m -= 1
    op = input().strip()

    if op == "all":
        s = set(range(1,21))
        continue
    elif op == "empty":
        s = set()
        continue
    
    op, num = op.split()
    num = int(num)
    if op == "add":
        s.add(num)
    elif op == "remove" and num in s:
        s.remove(num)
    elif op == "check":
        print(1) if num in s else print(0)
    elif op == "toggle":
        s.remove(num) if num in s else s.add(num)
    