n = input()

zero = n.count('0') // 2
one = n.count('1') // 2

answer = ''
for i in range(len(n)):
    if n[i] == '1':
        one -= 1
        if one == 0:
            answer += n[i+1:]
            break
        else:
            continue
    else:
        answer += '0'

answer = ''.join(list(reversed(list(answer))))
new_answer = ''
for i in range(len(answer)):
    if answer[i] == '0':
        zero -= 1
        if zero == 0:
            new_answer += answer[i+1:]
            break
        else:
            continue
    else:
        new_answer += '1'
    
new_answer = ''.join(list(reversed(list(new_answer))))
print(new_answer)