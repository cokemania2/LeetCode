from collections import deque

def solution(priorities, location):
    
    count = 0
    x = [1 if i == location else 0 for i in range(len(priorities))]
    priorities = deque(list(zip(x, priorities)))
    while len(priorities) > 0:
        max_priority = max([v[1] for v in priorities])
        x = priorities.popleft()
        if x[1] < max_priority:
            priorities.append(x)
        else:
            count += 1
            if x[0] == 1:
                return count
    return count