# https://www.acmicpc.net/problem/5430

from collections import deque

t = int(input())

while t != 0:
    p = list(input())
    n = int(input())
    temp = input()
    if n == 0:
        array = deque()
    else:
        array = deque(temp[1:-1].split(','))
    # print(array)

    status = True
    count = 0
    for i in p:
        if i == 'R':
            count += 1
        else:
            if not array:
                status = False
                break
            if count % 2 != 0:
                array.pop()
            else:
                array.popleft()
    if not status:
        print('error')
    else:
        if count % 2 != 0:
            array.reverse()
        print('[' + ','.join(array) + ']')

    t -= 1