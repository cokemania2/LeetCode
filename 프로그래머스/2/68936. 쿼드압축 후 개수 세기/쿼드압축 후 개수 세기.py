def devide(arr, y, x):
    length = len(arr) // 2
    if y == 0:
        arr = arr[:length]
    else:
        arr = arr[length:]
    if x == 0:
        new_arr = []
        for i in range(len(arr)):
            new_arr.append(arr[i][:length])
        arr = new_arr
    else:
        new_arr = []
        for i in range(len(arr)):
            new_arr.append(arr[i][length:])
        arr = new_arr
    return arr

            

def count_n(arr):
    dic = dict()
    if len(arr) == 2:
        for i in range(2):
            for j in range(2):
                if arr[i][j] in dic:
                    dic[arr[i][j]] += 1
                else:
                    dic[arr[i][j]] = 1
        if 1 not in dic:
            return 1, 0
        elif 0 not in dic:
            return 0, 1
        else:
            return dic[0], dic[1]
    else:
        a, b = count_n(devide(arr, 0, 0))
        c, d = count_n(devide(arr, 0, 1))
        e, f = count_n(devide(arr, 1, 0))
        g, h = count_n(devide(arr, 1, 1))
        if a == c == e == g == 1 and b == d == f == h == 0:
            return 1, 0
        elif a == c == e == g == 0 and b == d == f == h == 1:
            return 0, 1
        else:
            return a + c + e + g, b + d + f + h
            

def solution(arr):
    return count_n(arr)