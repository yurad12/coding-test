n = int(input())
horror = list(map(int, input().split()))
horror.sort()
count = 0

while(True):
    if not horror:
        break
    
    group = max(horror)
    if group <= n:
        horror.pop()
        del horror[:group-1]
    else:
        break
    count += 1
print(count)