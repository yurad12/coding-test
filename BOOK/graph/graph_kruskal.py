# 노드 개수와 간선 개수 입력받기
v, e = map(int,input().split())
parent = [0] * (v+1)

# 부모 테이블 초기화
for i in range(1,v+1):
	parent[i] = i

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 모든 간선에 대한 정보 입력 받기
for _ in range(e):
	a, b, cost = map(int,input().split())
	edges.append((cost,a,b))
# 간선을 비용순으로 정렬
edges.sort()

# 특정 원소가 속한 집합 찾기
def find_parent(parent,x):
	if parent[x] != x:
		parent[x] = find_parent(parent,parent[x])
	return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent,a,b):
	a = find_parent(parent,a)
	b = find_parent(parent,b)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b

# 간선을 하나씩 확인하며 사이클 발생하는지 보기
for edge in edges:
	cost, a, b = edge
	# 사이클이 발생하지 않는 경우에만 집합에 포함
	if find_parent(parent,a) != find_parent(parent,b):
		union_parent(parent,a,b)
		result += cost
print(result)