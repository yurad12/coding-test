import sys
n = int(sys.stdin.readline().rstrip())
storage = list(map(int,sys.stdin.readline().split()))
storage.sort()
m = int(sys.stdin.readline().rstrip())
f_product = list(map(int,sys.stdin.readline().split()))
# print(storage, f_product)

def binary_search(storage,product,start,end):
    while start <= end:
        mid = (start+end) // 2
        if storage[mid] == product:
            return True
        elif storage[mid] < product:
            start = mid+1
        elif storage[mid] > product:
            end = mid-1
    return False

for product in f_product:
    if n < m:
        break
    if binary_search(storage,product,0,n-1):
        print('yes', end=' ')
    else:
        print('no', end = ' ')
# print(binary_search(storage,3,0,n-1)) 