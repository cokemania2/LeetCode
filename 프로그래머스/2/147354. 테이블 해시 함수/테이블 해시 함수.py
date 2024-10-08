def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x: (x[col - 1], -x[0])) # 2
    
    s_i_list = [] # 3
    for i, d in enumerate(data):
        d_sum = 0
        for c in d:
            d_sum += c % (i + 1)
        s_i_list.append(d_sum)

    answer = s_i_list[row_begin - 1]
    for i in range(row_begin, row_end): # 4 
        answer ^= s_i_list[i]
        
    return answer