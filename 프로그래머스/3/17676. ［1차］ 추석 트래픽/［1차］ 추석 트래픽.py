import datetime

def solution(lines):
    date_list = []
    for line in lines:
        x = line.split(' ')
        time, duration = x[1], x[2][:-1]
        
        end_time = datetime.datetime.strptime(time, '%H:%M:%S.%f')
        duration = datetime.timedelta(seconds=float(duration))
        start_time = end_time - duration
        date_list.append([start_time + datetime.timedelta(milliseconds=1), 'a'])
        date_list.append([end_time + datetime.timedelta(milliseconds=999), 'b'])
    
    date_list.sort(key = lambda x: (x[0], x[1]))
    
    
    answer = 0
    _max = 0
    for date_time in date_list:
        
        if date_time[1] == "a":
            answer += 1
            if answer > _max:
                _max = answer
        else:
            answer -= 1
    return _max