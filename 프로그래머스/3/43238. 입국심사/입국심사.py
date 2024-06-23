def solution(n, times):
    answer = 0
    
    times = sorted(times)
    min_time = 0
    max_time = times[-1] * n
    
    
    while min_time < max_time:
        target_time = min_time + (max_time - min_time) // 2
        passed_people = 0
        for immigration_time in times:
            passed_people += (target_time // immigration_time)
            if passed_people >= n:
                break
        if passed_people >= n:
            max_time = target_time
        else:
            min_time = target_time + 1
    return min_time