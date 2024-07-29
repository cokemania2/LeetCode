from itertools import permutations

def generate_unique_numbers():
    digits = '123456789'
    permutations_list = list(permutations(digits, 3))
    return [''.join(perm) for perm in permutations_list]

# 생성된 숫자 모음 출력
unique_numbers = generate_unique_numbers()

n = int(input())
candi = unique_numbers
for i in range(n):
    hint, strike, ball = input().split()
    new_candi = []
    for number in candi:
        _strike = 0
        _ball = 0
        hint_arr = list(hint)
        for i in range(3):
            if number[i] == hint[i]:
                _strike += 1 
            if number[i] in hint_arr:
                _ball += 1
        _ball -= _strike
        if _ball == int(ball) and _strike == int(strike):
            new_candi.append(number)
    candi = new_candi
print(len(candi))