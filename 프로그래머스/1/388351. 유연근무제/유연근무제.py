# 출근 희망 시간 + 10분까지 어플로 출근

def log_to_minute(time):
    _time = str(time)
    hour = int(_time[:-2])
    minute = int(_time[-2:])
    return minute + hour * 60

def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        schedule, timelog = log_to_minute(schedules[i]), timelogs[i]
        for i, log in enumerate(timelog):
            if (startday + i - 1) % 7 + 1 in [6, 7]:
                continue
            if log_to_minute(log) > schedule + 10: # 지각
                break
        else:
            answer += 1
            
    return answer