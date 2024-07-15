# N = 10
# 가장 가까운 제곱 수 16 = 4^2, 16*2 = 32 크기 배열 필요
# 넉넉하게 4배 크기로 설정
arr = list(range(1,11))
tree = [0] * (len(arr)*4)

## 세그먼트 트리 채우기
# start: 시작 인덱스, end: 마지막 인덱스, idx: 트리 인덱스
def build_tree(start, end, idx):
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
    mid = (start + end) // 2
    tree[idx] = build_tree(start, mid, idx*2) + \
        build_tree(mid+1, end, idx*2+1)
    return tree[idx]

build_tree(0, len(arr)-1, 1)
print(tree)

## 구간 합 구하기
# left, right: 구간 합 범위
def get_prefix_sum(start, end, idx, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[idx]
    mid = (start + end) // 2
    return get_prefix_sum(start, mid, idx*2, left, right) + \
        get_prefix_sum(mid+1, end, idx*2+1, left, right)

print(get_prefix_sum(0, len(arr)-1, 1, 0, 9)) # 55
print(get_prefix_sum(0, len(arr)-1, 1, 2, 4)) # 12 = 3 + 4 + 5

## 특정 원소 값 수정하기
# a + c -> b
# node: 수정할 노드, value: 수정할 값
def update(start, end, idx, node, value):
    if node < start or end < node:
        return
    tree[idx] += value
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, idx*2, node, value)
    update(mid+1, end, idx*2+1, node, value)

print(get_prefix_sum(0, len(arr)-1, 1, 0, 8)) # 45
update(0, len(arr)-1, 1, 3, 2) # node 3 값(40) +2
print(get_prefix_sum(0, len(arr)-1, 1, 0, 8)) # 47


