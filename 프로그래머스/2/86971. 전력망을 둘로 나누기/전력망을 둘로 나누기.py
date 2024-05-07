def solution(n, wires):
    answer = n
    for severed_wires in (wires[i+1:] + wires[:i] for i in range(len(wires))):
        a_group = set(severed_wires[0])
        for _ in severed_wires:
            for severed_wire in severed_wires:
                if set(severed_wire) & a_group:
                    a_group.update(severed_wire)
        answer =  min(answer, abs(2 * len(a_group) - n))
    return answer
