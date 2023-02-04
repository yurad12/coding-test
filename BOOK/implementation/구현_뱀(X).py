#### xxxxx틀림xxxxx ####

# 게임 시작하고 x초 후에 왼쪽(L) 오른쪽(D), 벽 또는 자기자신과 부딪히면 게임 끝남
# 방향?
n = int(input())
k = int(input())
apple_loc = [list(map(int, input().split())) for _ in range(k)]
#print(apple_loc)
l = int(input())
t = [list(map(str, input().split())) for _ in range(l)]
trans = {}
for k in range(l):
    trans[int(t[k][0])] = t[k][1]
    if trans[int(t[k][0])] == 'D':
        trans[int(t[k][0])] = 'R'
#print(trans)

sec = 0
direction = 'R'
length = 1
head = [1,1]
body = [[1,1]]
tail = []
#print(trans.keys())

while(True):
    #탈출조건 
    if ((head[0]<1)|(head[1]<1)|(head[0]>n)|(head[1]>n))&(length>1):
        break
    elif (head in body[:length-1]) & (length>1):
        break
    elif (head==tail) & (length>1):
        break

    sec += 1

    #머리위치
    if direction=='R':
        head = [head[0],head[1]+1]
    elif direction=='L':
        head = [head[0],head[1]-1]
    elif direction=='U':
        head = [head[0]-1,head[1]]
    elif direction=='D':
        head = [head[0]+1,head[1]]
    
    #사과위치, 몸통위치
    body.append(head)
    if head in apple_loc:
        length += 1
        apple_loc.remove(head)
    else:
        tail = body[0]
        body.pop(0)


    # print('sec',sec)
    # print('1d',direction)
    #방향전환
    if sec in trans.keys():
        if trans[sec] == direction:
            direction = 'D'
        elif (trans[sec]!=direction) & (direction in ['R','L']):
            direction = 'U'
        elif ((trans[sec]=='R')&(direction=='D')) | ((trans[sec]=='L')&(direction=='U')):
            direction = 'L'
        elif ((trans[sec]=='R')&(direction=='U')) | ((trans[sec]=='L')&(direction=='D')):
            direction = 'R'

    # print('2d',direction)
    print('next_head:', head)
    print('body', body)
        

print(sec)