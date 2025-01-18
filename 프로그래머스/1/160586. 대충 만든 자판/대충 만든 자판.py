def solution(keymap, targets):
    answer = [0 for _ in range(len(targets))]
    
    key_map = dict()
    for i, key in enumerate(keymap):
        for j, v in enumerate(key):
            if v in key_map:
                key_map[v] = [i, min(key_map[v][1], j + 1)]
            else:
                key_map[v] = [i, j + 1]
    
    for i, target in enumerate(targets):
        for v in target:
            if v not in key_map:
                answer[i] = -1
                break
            _, count = key_map[v]
            answer[i] += count
    

    return answer