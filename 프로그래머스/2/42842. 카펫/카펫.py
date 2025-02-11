import math

# 색상 상관없이 가로 세로로 넓이 맞추면 됌
# (가로 - 2) * (세로 -2) = 노랑의 넓이 (갯수)

def solution(brown, yellow):
    answer = []
    
    area = brown + yellow
    max_height = int(math.sqrt(area))
    for height in range(1, max_height + 1):
        width = area // height
        if (width - 2) * (height - 2) == yellow:
            return [width, height]