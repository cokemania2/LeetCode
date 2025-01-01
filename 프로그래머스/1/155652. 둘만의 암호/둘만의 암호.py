def solution(s, skip, index):
    answer = ''
    skip_asciis = list(map(ord, list(skip)))
    for v in s:
        count = 0
        v_ascii = ord(v)
        while count < index:
            v_ascii += 1  # 문자 이동
            if v_ascii > ord('z'):  # z를 초과하면 a로 돌아감
                v_ascii = ord('a')
            if v_ascii in skip_asciis:  # skip 문자는 무시
                continue
            count += 1  # 유효한 이동일 경우에만 증가
        answer += chr(v_ascii)
    return answer