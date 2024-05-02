import string

def solution(msg):
    answer = []
    
    # A부터 Z까지의 알파벳
    alphabet = string.ascii_uppercase
    # 알파벳에 번호를 매기는 딕셔너리 생성
    compression_dict = {char: index + 1 for index, char in enumerate(alphabet)}

    msg_index = 1
    dict_index = 27
    while len(msg) != 0:
        while msg[:msg_index] in compression_dict:
            if msg_index == len(msg):
                answer.append(compression_dict[msg])
                return answer
            msg_index += 1
        answer.append(compression_dict[msg[:msg_index - 1]])
        compression_dict[msg[:msg_index]] = dict_index
    
        msg = msg[msg_index-1:]
        msg_index = 1
        dict_index += 1
        
    return answer