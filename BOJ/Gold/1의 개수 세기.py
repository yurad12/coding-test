# https://www.acmicpc.net/problem/9527
'''
(00) 01 10 11 100 101 110 111
1000 1001 1010 1011 1100 1101 1110 1111
-> 01 01 01 01, 0011 00111, 00001111 000011111
-> 2^k번마다 1, 0이 나타남
'''

A, B = map(int, input().split())

def func(n):
    if n <= 0:
        return 0
    
    count = 0
    i = 0
    while (1 << i) <= n:
        # 비트 반복하는 구간
        block = (n+1) // (1 << (i+1))

        # 블록 크기 2(0 bit, 1번): 0-1, 4(1 bit, 2번): 0-3/4-7, 8(2 bit, 4번): 0-7/8-15
        count += block * (1 << i)

        # 블록 크기가 8이면, 0-7는 한 블록이고, 8-12는 나머지 부분
        # 그러니까 나머지에서 해당 비트가 1이 되는 경우를 추가로 계산
        r = (n+1) % (1 << (i+1))
        if r > (1 << i):
            count += r - (1 << i)

        i += 1

    return count

answer = func(B) - func(A-1)
print(answer)