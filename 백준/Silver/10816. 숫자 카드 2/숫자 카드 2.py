from collections import Counter

N = int(input())
card_list = list(map(int, input().split()))
M = int(input())
m_list = list(map(int, input().split()))

def is_exist(sorted_card_list, m):
    start = 0
    end = len(sorted_card_list) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if sorted_card_list[mid] == m:
            return True
        elif sorted_card_list[mid] < m:
            start = mid + 1
        else:
            end = mid - 1
    return False

def solution(N, M, card_list, m_list):
    answer = []
    
    card_counter = Counter(card_list)
    card_list = list(set(card_list))
    card_list.sort()
    for m in m_list:
        if is_exist(card_list, m):
            answer.append(card_counter[m])
        else:
            answer.append(0)
    return answer

def print_solution(answer_list):
    for answer in answer_list:
        print(answer, end=' ')

print_solution(solution(N, M, card_list, m_list))