# 거꾸로 뒤집고, 나보다 큰친구의 큰친구의 갯수 + 1 기록 

def solution(prices):
    answer = []
    
    for i in range(len(prices) -1):
        x = 1
        for j in range(i + 1, len(prices) -1):
            if prices[i] <= prices[j]:
                x += 1
            else:
                break
        answer.append(x)
    answer.append(0)
    return answer