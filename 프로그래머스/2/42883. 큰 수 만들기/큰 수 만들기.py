def recursive_pop(stack, number, k):
    if k > 0 and len(stack) > 0 and stack[-1] < number:
        k -= 1
        stack.pop()
        return recursive_pop(stack, number, k)
    return k

def solution(number, k):
    stack = []
    x = k
    for i in range(len(number)):
        if k > 0:
            k = recursive_pop(stack, number[i], k)
        stack.append(number[i])
    
    return ''.join(stack)[:len(stack)-k]
