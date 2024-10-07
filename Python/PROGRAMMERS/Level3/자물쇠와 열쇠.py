# https://school.programmers.co.kr/learn/courses/30/lessons/60059

def rotate(array):
    r = len(array)
    c = len(array[0])
    new_array = [[0]*r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            new_array[j][r-1-i] = array[i][j]
    return new_array

def find(array):
    key_set = set()
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]:
                key_set.add((i,j))
    return key_set

def check(status,loc,key,lock):
    n = len(lock)
    for i in range(len(key)):
        for j in range(len(key[0])):
            if status == "+" and key[i][j]:
                x, y = i+loc, j+loc
                if x >= 0 and x < n and y >= 0 and y < n and lock[x][y]:
                    return False
            elif status == "-" and key[i][j]:
                x, y = i-loc, j-loc
                if x >= 0 and x < n and y >= 0 and y < n and lock[x][y]:
                    return False
    return True

def solution(key, lock):
    lock_set = set()
    for i in range(len(lock)):
        for j in range(len(lock[0])):
            if not lock[i][j]:
                lock_set.add((i,j))
    n = len(lock_set)
    
    for r in range(4):
        key = rotate(key)
        key_set = find(key)
        
        # plus
        count = 0
        for k in key_set:
            px = k[0] + 1
            py = k[1] + 1
            if (px,py) in lock_set:
                count += 1
        if count == n:
            return check("+",i,key,lock)
        
        # minus
        count = 0
        for k in key_set:
            mx = k[0] - 1
            my = k[1] - 1
            if (px,py) in lock_set:
                count += 1
        if count == n:
            return check("-",i,key,lock)

    return False