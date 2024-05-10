def rebase(n, q):
    rev_base = ''
    str_list=list("0123456789ABCDEF")
    
    if n == 0:
        return '0'
    
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str_list[mod]

    return rev_base[::-1]

def solution(n, t, m, p):
    answer = ''
    
    s = "".join([rebase(i, n) for i in range(m * t)])
    for i in range(t):
        split_s = s[:m]
        s = s[m:]
        answer += split_s[p - 1]
    return answer