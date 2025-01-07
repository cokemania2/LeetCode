def solution(players, callings):
    answer = players
    index_dict = dict()
    index = 0 
    
    for player in players:
        index_dict[player] = index
        index += 1
    
    for calling in callings:
        front_index = index_dict[calling] - 1
        back_index = index_dict[calling]
        
        temp = answer[front_index]
        answer[front_index] = answer[back_index]
        answer[back_index] = temp
        
        index_dict[answer[front_index]] = front_index
        index_dict[answer[back_index]] = back_index
        
    return answer