def solution(babbling):
    answer = 0
    
    x_list = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        start_index = 0
        before_word = ""
        while start_index < len(b):
            for x in x_list:
                if b[start_index:start_index+len(x)] == x and before_word != x:
                    start_index += len(x)
                    before_word = x
                    break
            else:
                break
        if start_index == len(b):
            answer += 1
    
    return answer