def _prev(time):
    return max(time - 10, 0)

def _next(time, last_time):
    return min(time + 10, last_time)


def time_to_sec(time):
    minute, sec = time.split(":")
    return int(minute) * 60 + int(sec)

def sec_to_time(sec):
    minute = str(sec // 60) 
    if len(minute) == 1:
        minute = "0" + minute
    sec = str(sec % 60)
    if len(sec) == 1:
        sec = "0" + sec
    return minute + ":" + sec
    


def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    pos = time_to_sec(pos)
    last_time = time_to_sec(video_len)
    op_start = time_to_sec(op_start)
    op_end = time_to_sec(op_end)
    for command in commands:
        if pos >= op_start and pos <= op_end:
            pos = op_end
        if command == "prev":
            pos = _prev(pos)
        elif command == "next":
            pos = _next(pos, last_time)
        if pos >= op_start and pos <= op_end:
            pos = op_end
    return sec_to_time(pos)