def solution(bandage, health, attacks):
    answer = 0
    max_halth = health
    before_time = attacks[0][0] - 1
    for attck in attacks:
        time, damage = attck
        used_time = time - before_time - 1
        before_time = time
        continous_usage = (used_time * bandage[1])
        additional_recovery = (used_time // bandage[0]) * bandage[2]
        health = min(max_halth, health + continous_usage + additional_recovery)
        health -= damage
        if health <= 0:
            return -1
        
    return health