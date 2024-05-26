import math

INF = math.inf

def solution(n, s, a, b, fares):
    distances = [[INF for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == j:
                distances[i][j] = 0

    for n1, n2, distance in fares:
        distances[n1 - 1][n2 - 1] = distance
        distances[n2 - 1][n1 - 1] = distance

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
    
    return min([distances[s - 1][t] + distances[t][a - 1] + distances[t][b - 1] for t in range(n)])