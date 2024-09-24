# https://school.programmers.co.kr/learn/courses/30/lessons/42888

# sol1
def solution(record):
    info = {}
    for rec in record:
        r = list(rec.split(' '))
        if r[0] == "Leave":
            continue
        
        uid, nickname = r[1], r[2]
        if uid not in info:
            info[uid] = ''
        info[uid] = nickname

    answer = []
    for rec in record:
        r = list(rec.split(' '))
        sign, uid = r[0], r[1]
        
        if sign == "Enter":
            answer.append("%s님이 들어왔습니다." %info[uid])
        elif sign == "Leave":
            answer.append("%s님이 나갔습니다." %info[uid])
    
    return answer

# sol2
def solution(record):
    printer = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    info = {}
    for rec in record:
        r = list(rec.split(' '))
        if r[0] == "Leave":
            continue
        info[r[1]] = r[2]

    answer = []
    for rec in record:
        r = list(rec.split(' '))
        if r[0] == "Change":
            continue
        answer.append(info[r[1]] + printer[r[0]])
    
    return answer