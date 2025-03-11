def solution(n, w, num):
    boxes = []
    box_row = []
    for i in range(n):
        if i % w == 0 and len(box_row) > 0:
            if len(boxes) % 2 == 1:
                box_row.reverse()
            boxes.append(box_row)
            box_row = []
        box_row.append(i + 1)
    
    if len(box_row) > 0:
        for i in range(w - len(box_row)):
            box_row.append(0)
        if len(boxes) % 2 == 1:
            box_row.reverse()
        boxes.append(box_row)
    boxes.reverse()
    
    for i, box in enumerate(boxes):
        if box.count(num) != 0:
            answer = i + 1
            index = box.index(num)
            if boxes[0][index] == 0:
                answer -= 1
    return answer