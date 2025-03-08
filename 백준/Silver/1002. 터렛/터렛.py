def get_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def cant_meet(a, b, a_b_distance):
    # 외부에서 만나지 않음
    if a_b_distance > a[2] + b[2]:
        return True
    
    # 내부에 포함되는 경우
    if max(a[2], b[2]) > a_b_distance + min(a[2], b[2]):
        return True

    # 동심원인 경우
    if a_b_distance == 0 and a[2] != b[2]:
        return True

    return False

def meet_once(a, b, a_b_distance):
    # 외접하는 경우
    if (a[1] != b[1] or a[0] != b[0]):
        if a_b_distance == a[2] + b[2]:
            return True

        # 내접하는 경우
        if a_b_distance == max(a[2], b[2]) - min(a[2], b[2]):
            return True
    return False
    
def meet_twice(a, b, a_b_distance):
    # 두 점에서 만나는 경우
    if (a[1] != b[1] or a[0] != b[0]) and a_b_distance < a[2] + b[2]:
        return True

    return False



def get_location(a, b):
    a_b_distance = get_distance(a[0], a[1], b[0], b[1])
    
    if cant_meet(a, b, a_b_distance):
        return 0
    elif meet_once(a, b, a_b_distance):
        return 1
    elif meet_twice(a, b, a_b_distance):
        return 2
    return -1
    

T = int(input())
for i in range(T):
    locations = list(map(int, input().split()))
    a = locations[:3]
    b = locations[3:6]
    
    print(get_location(a, b))
    
    