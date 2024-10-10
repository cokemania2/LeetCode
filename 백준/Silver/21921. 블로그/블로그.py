
def solution(x, visitors):
    if sum(visitors) == 0:
        return "SAD"

    left = 0
    right = x
    maxx = 0
    max_count = 0
    summ = sum(visitors[left:right])
    while True:
        if summ > maxx:
            maxx = summ
            max_count = 1
        elif summ == maxx:
            max_count += 1 
        if right == len(visitors):
            break
        summ -= visitors[left]
        summ += visitors[right]

        left += 1 
        right += 1


    return f"{maxx}\n{max_count}"


n, x = map(int, input().split())
visitors = list(map(int, input().split()))
print(solution(x, visitors))