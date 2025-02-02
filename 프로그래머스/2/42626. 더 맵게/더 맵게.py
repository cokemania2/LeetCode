import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while True:
        min_n_1 = heapq.heappop(scoville)
        if len(scoville) < 1 and min_n_1 < K:
            return -1
        if min_n_1 >= K:
            return answer
        min_n_2 = heapq.heappop(scoville)
        
        heapq.heappush(scoville, min_n_1 + min_n_2 * 2)
        answer += 1

    return answer