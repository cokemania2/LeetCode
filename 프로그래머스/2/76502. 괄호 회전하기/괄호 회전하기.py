from collections import deque

def is_valid(s_list):
    stack = []
    
    for s in s_list:
        if len(stack) > 0 and (s == ')' and stack[-1] == '(' or s == '}' and stack[-1] == '{' or s == ']' and stack[-1] == '['):
            stack.pop()
        else:
            stack.append(s)
    return True if len(stack) == 0 else False
        
def solution(s):
    answer = 0
    s_list = deque(list(s))
    
    for i in range(len(s)):
        s_list.append(s_list.popleft())
        if is_valid(s_list):
            answer += 1
    
    return answer