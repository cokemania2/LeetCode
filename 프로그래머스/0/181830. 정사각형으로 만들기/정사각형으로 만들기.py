def solution(arr):
    y_length = len(arr)
    x_length = len(arr[0])
    for v in arr:
        for i in range(y_length - x_length):
            v.append(0)
    for i in range(x_length - y_length): 
        arr.append([0 for _ in range(x_length)])
    
    return arr