# 수평2칸+수직1칸, 수직2칸+수평1칸
# 위/아래, 왼/오 2칸씩 여유가 있는가?
# temp[0]:열, temp[1]:행

loc = input()
dict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
trans = [[-2,-1],[-2,1],[2,-1],[2,1],[-1,2],[1,2],[-1,-2],[1,-2]]
loc = [dict[loc[0]],int(loc[1])]
answer = 0

for i in trans:
    temp = [i + loc for i,loc in zip(i,loc)]
    print(temp)
    if (0<temp[0]<9) & (0<temp[1]<9):
        answer += 1
    print(answer)

print(answer)