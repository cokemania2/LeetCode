from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge_weight = deque([0 for _ in range(bridge_length)])
    truck_weights.reverse()
    trucks_on_bridge = 0
    while len(truck_weights) > 0 or trucks_on_bridge != 0:
        out_truck = bridge_weight.popleft()
        if out_truck > 0:
            trucks_on_bridge -= out_truck
        if len(truck_weights) > 0 and trucks_on_bridge + truck_weights[-1] <= weight:
            next_truck = truck_weights.pop()
            bridge_weight.append(next_truck)
            trucks_on_bridge += next_truck
        else:
            bridge_weight.append(0)
        answer += 1
    
    return answer