# https://school.programmers.co.kr/learn/courses/30/lessons/17678

def solution(n, t, m, timetable):
    def time_to_minutes(time):
        h, m = map(int, time.split(":"))
        return h * 60 + m
    
    def minutes_to_time(minutes):
        h = minutes // 60
        m = minutes % 60
        return str(h).zfill(2) + ":" + str(m).zfill(2)
     
    N = len(timetable)
    timetable = sorted([time_to_minutes(time) for time in timetable])
    cur_time = time_to_minutes("09:00")
    idx = 0
    answer = ''
    
    for i in range(n):
        cur_m = 0
        while idx < N and timetable[idx] <= cur_time and cur_m < m:
            cur_m += 1
            idx += 1
        
        if i == n-1:
            if cur_m < m:
                answer = cur_time
            else:
                cur_time = timetable[idx-1] - 1
        else:
            cur_time += t
    
    answer = minutes_to_time(cur_time)
    return answer