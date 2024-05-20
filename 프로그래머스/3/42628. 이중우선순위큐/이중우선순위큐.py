import heapq

def solution(operations):
    hq = []
    for operation in operations:
        c, n = operation.split(' ')
        n = int(n)
        if c == "I":
            heapq.heappush(hq, n)
        elif len(hq) != 0:
            if n == -1:
                heapq.heappop(hq)
            else:
                hq.sort()
                hq.pop(-1)
    hq.sort()
    return [0, 0] if len(hq) == 0 else [hq[-1], hq[0]]