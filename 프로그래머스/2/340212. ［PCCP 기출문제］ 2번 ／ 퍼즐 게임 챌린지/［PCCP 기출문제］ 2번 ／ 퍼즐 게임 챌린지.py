def get_spend_time(level, diffs, times):
    total_time = 0
    for i in range(len(diffs)):
        # 기본적으로 현재 퍼즐을 푸는 시간 추가
        total_time += times[i]
        
        # 숙련도가 부족하면 틀리는 횟수만큼 추가 시간 소요
        if diffs[i] > level:
            mistakes = diffs[i] - level
            # 틀릴 때마다 현재 퍼즐 시간 + 이전 퍼즐 시간
            current_penalty = times[i]
            prev_penalty = times[i-1] if i > 0 else 0
            total_time += (current_penalty + prev_penalty) * mistakes
    
    return total_time

def solution(diffs, times, limit):
    left, right = 1, max(diffs)  # 최대 난이도까지만 탐색하면 충분
    result = right  # 초기값은 최대값으로 설정
    
    while left <= right:
        mid = left + (right - left) // 2
        spend_time = get_spend_time(mid, diffs, times)
        
        if spend_time <= limit:
            # 가능한 경우, 결과 업데이트 후 더 작은 level 탐색
            result = mid
            right = mid - 1
        else:
            # 불가능한 경우, 더 큰 level 탐색
            left = mid + 1
            
    return result