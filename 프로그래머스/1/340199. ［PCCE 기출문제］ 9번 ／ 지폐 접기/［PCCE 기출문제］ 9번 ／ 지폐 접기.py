def solution(wallet, bill):
    answer = 0
    wallet.sort()
    while True:
        bill.sort()
        if bill[1] <= wallet[1] and bill[0] <= wallet[0]:
            return answer
        bill[1] //= 2
        answer += 1 
    
    return answer