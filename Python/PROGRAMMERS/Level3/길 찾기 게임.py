# https://school.programmers.co.kr/learn/courses/30/lessons/42892?language=python3

import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    # 중위순회 6 9 4 1 5 8 7 2 3
    nodes = [(i+1, node) for i, node in enumerate(nodeinfo)]
    nodes.sort(key = lambda x: x[1][0])
    
    def preorder(nodes, root_idx):
        if not nodes:
            return []
        
        node = nodes[root_idx][0]
        left = nodes[:root_idx]
        right = nodes[root_idx+1:]
        left_idx = max(range(len(left)), key = lambda x: left[x][1][1]) if left else None
        right_idx = max(range(len(right)), key = lambda x: right[x][1][1]) if right else None
        
        return [node] + \
            (preorder(left, left_idx) if left_idx is not None else []) +  \
            (preorder(right, right_idx) if right_idx is not None else [])
        
    def postorder(nodes, root_idx):
        if not nodes:
            return []
        
        node = nodes[root_idx][0]
        left = nodes[:root_idx]
        right = nodes[root_idx+1:]
        left_idx = max(range(len(left)), key = lambda x: left[x][1][1]) if left else None
        right_idx = max(range(len(right)), key = lambda x: right[x][1][1]) if right else None
        
        return (postorder(left, left_idx) if left_idx is not None else []) +  \
            (postorder(right, right_idx) if right_idx is not None else []) + \
            [node]
        

    root_idx = max(range(len(nodes)), key = lambda x: nodes[x][1][1])
    preordered = preorder(nodes, root_idx)
    postordered = postorder(nodes, root_idx)
    
    answer = [preordered, postordered]
    return answer