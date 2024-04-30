'''
https://school.programmers.co.kr/learn/courses/30/lessons/49993#fn1

1. 먼저 배워야 하는 스킬 순서에 따라 숫자를 매긴 딕셔너리 만들기
2. 이중 반복문을 사용하여 모든 스킬트리에 대해 각각의 스킬이 배워야하는 스킬 순서에 있을 때 해당 스킬이 다음 가중치와 일치하면 가중치에 1증가하고 그게 아니라면 잘못된 스킬트리이므로 반복문을 멈춘다.
3. flag가 true라면 가능한 스킬트리이므로 1증가한다.
'''

def solution(skill, skill_trees):
    answer = 0
    
    # skill 종류: 1~26가지
    # skill 순서에 따라 중요도 주기
    skill_weight = dict()
    for i in range(len(skill)):
        skill_weight[skill[i]] = i+1

    for skill_tree in skill_trees:
        weight = 0
        flag = True
        
        for skill in skill_tree:
            if skill in skill_weight:
                if skill_weight[skill] == weight+1:
                    weight += 1
                else:
                    flag = False
                    break
        if flag:
            answer += 1
    
    return answer