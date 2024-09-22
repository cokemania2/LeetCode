def solution(wallpaper):
    answer = []
    
    min_x = len(wallpaper[0])
    min_y = len(wallpaper)
    max_x = 0
    max_y = 0

    for y in range(len(wallpaper)):
        for x in range(len(wallpaper[0])):
            if wallpaper[y][x] == "#":
                min_x = min(min_x, x)
                min_y = min(min_y, y)
                max_x = max(max_x, x)
                max_y = max(max_y, y)
                
    return [min_y, min_x, max_y + 1, max_x + 1]