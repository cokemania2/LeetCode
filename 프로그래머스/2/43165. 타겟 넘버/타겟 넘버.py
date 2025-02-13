def DFS(numbers, number_sum, index, target): 
    if index == len(numbers):
        return 1 if number_sum == target else 0
    
    return (DFS(numbers, number_sum + numbers[index], index + 1, target) + 
            DFS(numbers, number_sum - numbers[index], index + 1, target))

def solution(numbers, target):
    return DFS(numbers, 0, 0, target)