
def find_head(a, n) -> [int, int]:
    # 처음 나오는 * 이 머리가 된다.
    for y in range(n):
        for x in range(n):
            if a[y][x] == "*":
                return (y, x)

def find_arms(heart, a, n) -> [int, int]:
    left = right = 0
    while heart[1] + left >= 0 and a[heart[0]][heart[1] + left] == "*":
        left -= 1
    while heart[1] + right < n and a[heart[0]][heart[1] + right] == "*":
        right += 1
    return -(left + 1), (right -1)

def find_waist(heart, a, n) -> int:
    length = 0
    while heart[0] + length < n and a[heart[0]+ length][heart[1]] == "*":
        length += 1
    return length - 1 

def find_legs(heart, waist, a, n) -> [int, int]:
    last_waist = heart[0] + waist
    left_leg_start = [last_waist + 1, heart[1] - 1]
    right_leg_start = [last_waist + 1, heart[1] + 1]

    left_length = 0
    right_length = 0

    while left_leg_start[0] + left_length < n and a[left_leg_start[0] + left_length][left_leg_start[1]] == "*":
        left_length += 1

    while right_leg_start[0] + right_length < n and a[right_leg_start[0] + right_length][right_leg_start[1]] == "*":
        right_length += 1

    return left_length, right_length

n = int(input())
a = []
for i in range(n):
    a.append(list(input()))

y, x = find_head(a, n)
heart = [y + 1, x]
arm_lengh = find_arms(heart, a, n)
waist_length = find_waist(heart, a, n)
legs_length = find_legs(heart, waist_length, a, n)

print(heart[0] + 1, heart[1] + 1)
print(arm_lengh[0], arm_lengh[1], waist_length, legs_length[0], legs_length[1])
