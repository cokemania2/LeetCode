def solution(routes):
    answer = 0
    
    routes.sort(key= lambda x: (x[0], x[1]))
    camera_count = 1
    camera = routes[0][1]
    for i in range(1, len(routes)):
        if camera < routes[i][0]:
            camera_count += 1
            camera = routes[i][1]
        if routes[i][1] < camera:
            camera = routes[i][1]
    return camera_count

