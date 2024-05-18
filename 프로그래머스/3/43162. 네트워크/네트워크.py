def check_network(computers, check_arr, i):
    for i, computer in enumerate(computers[i]):
        if check_arr[i] is False and computer == 1:
            check_arr[i] = True
            check_arr = check_network(computers, check_arr, i)
    return check_arr

def solution(n, computers):
    answer = 0
    check_arr = [False for _ in range(len(computers))]
    
    for i in range(len(computers)):
        if check_arr[i] is False:
            check_arr = check_network(computers, check_arr, i)
            answer += 1
    return answer