from collections import deque

def create_dict(n):
    # 딕셔너리를 생성하여 1부터 n까지의 숫자를 키로 설정
    return {i: -1 for i in range(1, n + 1)}

def save_short_cuts(destination, map_dict, road_dict):
    queue = deque([[destination, 0]])
    
    while queue:
        road, count = queue.popleft()
        if map_dict[road] == -1 or map_dict[road] > count:
            map_dict[road] = count
        
            next_roads = road_dict[road]
            for next_road in next_roads:
                queue.append([next_road, count + 1])
            

def input_to_dict(a, b, dic):
    if a in dic:
        dic[a].append(b)
    else:
        dic[a] = [b]

def solution(n, roads, sources, destination):
    answer = []
    road_dict = dict()
    
    for road in roads:
        input_to_dict(road[0], road[1], road_dict)
        input_to_dict(road[1], road[0], road_dict)
    
    map_dict = create_dict(n)
    save_short_cuts(destination, map_dict, road_dict)
    
    for source in sources:
        answer.append(map_dict[source])
    
    return answer