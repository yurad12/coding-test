case = int(input())
people_list = {}
#1:14
#1,3,6,...,SUM(1:14)

for i in range(case):
    floor = int(input())
    room = int(input())
    #print('fr',floor,room)

    for j in range(floor+1):
        if j==0:
            people_list[j] = [k+1 for k in range(14)]
        else:
            people_list[j] = [sum(people_list[j-1][:k+1]) for k in range(14)]
    #print(people_list)    
    print(people_list[floor][room-1])