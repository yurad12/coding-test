# https://school.programmers.co.kr/learn/courses/30/lessons/17683#

def solution(m, musicinfos):
    def convert(sheet):
        sheet = sheet.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
        return sheet
    
    m = convert(m)
    max_count = 0
    answer = ''
    
    for info in musicinfos:
        start, end, name, sheet = info.split(',')
        st, sm = start.split(':')
        et, em = end.split(':')
        minutes = (int(et)-int(st)) * 60 + (int(em)-int(sm))
        
        sheet = convert(sheet)
        if len(sheet) > minutes:
            sheet = sheet[:minutes]
        else:
            sheet = sheet * (minutes // len(sheet)) + (sheet[:len(sheet) % minutes])

        if m in sheet and minutes > max_count:
            max_count = minutes
            answer = name
        
    if not answer:
        answer = '(None)'

    return answer