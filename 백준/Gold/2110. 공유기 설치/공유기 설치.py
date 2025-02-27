import sys

def is_eqaul_or_over_setting_count(homes, distance, C):
    count = 1  # 첫 번째 집에 공유기 설치
    last_router = homes[0]  # 마지막 공유기가 설치된 집
    
    for i in range(1, len(homes)):
        if homes[i] - last_router >= distance:
            count += 1
            last_router = homes[i]  # 공유기 설치 후 위치 갱신

    return count >= C  # C개 이상 공유기를 설치할 수 있는지 확인

def binary_search(homes, C):
    left = 1  # 최소 거리 (공유기 간 거리는 최소 1 이상)
    right = homes[-1] - homes[0]  # 최대 거리 (가장 멀리 떨어진 집 간 거리)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        
        if is_eqaul_or_over_setting_count(homes, mid, C):
            answer = mid  # 가능한 경우, 정답을 업데이트
            left = mid + 1  # 더 큰 거리 탐색
        else:
            right = mid - 1  # 거리를 줄여서 다시 탐색
    
    return answer

def solution():
    N, C = map(int, input().split())

    homes = []
    for _ in range(N):
        homes.append(int(sys.stdin.readline().strip()))

    homes.sort()  # 좌표 정렬 필수
    answer = binary_search(homes, C)
    return answer

print(solution())