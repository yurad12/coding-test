s = input()
count = 0

if len(set(list(s))) == 1:
    count = 0
else:
    count = (s.count('01')+s.count('10')+1)//2
print(count)