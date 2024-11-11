# https://www.acmicpc.net/problem/2922
import sys
input = sys.stdin.readline

word = list(input().strip())

vowels = {'A', 'E', 'I', 'O', 'U'}

def create(idx, now, total, l):
    global answer

    if now[0] == 3 or now[1] == 3:
        return
    if idx == len(word):
        if word.count('L') or l:
            answer += (5 ** total[0]) * (20 ** (total[1]-l))
        return

    if word[idx] == '_':
        create(idx+1, [now[0]+1, 0], [total[0]+1, total[1]], l)
        create(idx+1, [0, now[1]+1], [total[0], total[1]+1], l)
        create(idx+1, [0, now[1]+1], [total[0], total[1]+1], l+1)
    else:
        if word[idx] in vowels:
            create(idx+1, [now[0]+1, 0], total, l)
        else:
            create(idx+1, [0, now[1]+1], total, l)

answer = 0
create(0, [0,0], [0,0], 0)
print(answer)