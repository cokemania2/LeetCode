def solution(n, results):
    answer = 0
    
    check = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(len(results)):
        a, b = results[i]
        check[a - 1][b - 1] = 1
        check[b - 1][a - 1] = -1
            
    for k in range(n):                  
        for i in range(n):              
            for j in range(n):          
                if check[i][j] == 0:   
                    # i가 k보다 크고, k가 j보다 크다면
                    if check[i][k] == 1 and check[k][j] == 1:
                        # i가 j보다 크다
                        check[i][j] = 1
                    elif check[i][k] == -1 and check[k][j] == -1:
                        check[i][j] = -1
    for i in range(n):
        zero = 1
        for j in range(n):
            if check[i][j] == 0:
                zero -= 1
        if zero == 0:
            answer += 1
                
    return answer