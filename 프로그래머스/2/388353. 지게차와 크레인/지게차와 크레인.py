# A: 순간 접근 가능한 A 출고
#   0으로 기록하는 순간은 모두 출고 후 기록
# AA: 크레인을 이용해서 모든 A 출고
# 각 위치를 모두 저장해놓기
# 빠져나간 컨테이너의 위치는 0으로 기록

def check_zero(remain_list, storage):
    for remain in remain_list:
        storage[remain[0]][remain[1]] = '0'

def is_accessible(location, storage):
    if not storage or not storage[0]:
        return True
        
    rows, cols = len(storage), len(storage[0])
    visited = set()
    
    def dfs(y, x):            
        if (y, x) in visited or y < 0 or y >= rows or x < 0 or x >= cols or storage[y][x] != '0':
            return False

        # 가장자리에 도달하면 True 반환
        if y <= 0 or y >= rows-1 or x <= 0 or x >= cols-1:
            return True
        
        visited.add((y, x))
        
        # 상하좌우 탐색
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for dy, dx in directions:
            if dfs(y + dy, x + dx):
                return True
        return False
    
    # 현재 위치 주변에 '0'이 있으면 DFS 시작
    y, x = location
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 > ny or ny >= rows or 0 > nx or nx >= cols:
            return True
        if storage[ny][nx] == '0': 
            return dfs(ny, nx)
    return False

def get_by_forklift(container_locations, container, storage):
    """
    순간 접근 가능한 컨테이너 출고, 0으로 기록하는 순간은 모두 출고 후 기록
    """
    ship_out_list = []
    remain_list = []
    if container not in container_locations:
        return
    
    locations = container_locations[container]
    for location in locations:
        if is_accessible(location, storage):
            ship_out_list.append(location)

        else:
            remain_list.append(location)

    for v in ship_out_list:
        storage[v[0]][v[1]] = '0'

    container_locations[container] = remain_list

def get_by_crane(container_locations, container, storage):
    """
    크레인을 사용해서 컨테이너 출고
    """
    if container not in container_locations:
        return
        
    locations = container_locations[container]
    for location in locations:
        storage[location[0]][location[1]] = '0'
    
    container_locations[container] = []

def set_container_locations(storage):
    container_locations = dict()
    for i in range(len(storage)):
        storage[i] = list(storage[i])
        for j in range(len(storage[i])):
            if storage[i][j] != '0':
                if storage[i][j] in container_locations:
                    container_locations[storage[i][j]].append([i, j])
                else:
                    container_locations[storage[i][j]] = [[i, j]]
    return container_locations

def get_remain_container_count(storage):
    count = 0
    for i in range(len(storage)):
        for j in range(len(storage[i])):
            if storage[i][j] != '0':
                count += 1
    return count

def solution(storage, requests):
    answer = 0
    
    container_locations = set_container_locations(storage)

    for request in requests:
        container = request[0]
        if len(request) == 1:
            get_by_forklift(container_locations, container, storage)
        else:
            get_by_crane(container_locations, container, storage)
    
    answer = get_remain_container_count(storage)
    return answer