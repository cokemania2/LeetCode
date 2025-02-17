def solution(n):
    x = 1
    before = bin(n)[2:].count('1')
    while True:
        if bin(n + x)[2:].count('1') == before:
            break
        x += 1
    
    return n + x