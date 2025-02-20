def solution(players, m, k):
    answer = 0
    
    server_capacity = [m for _ in range(24)]
    for i in range(24):
        if server_capacity[i] <= players[i]:
            server_needed = (players[i] - server_capacity[i]) // m + 1
            answer += server_needed
            
            for j in range(i, min(i+k, 24)):
                server_capacity[j] += (server_needed) * m
    return answer
