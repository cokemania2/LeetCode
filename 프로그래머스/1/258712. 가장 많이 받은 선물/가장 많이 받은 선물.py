"""
1. dictionary로 준 선물, 받은선물 기록
2. 선물 증정 알고리즘 타기
3. 정렬 후 리턴
"""

def solution(friends, gifts):
    answer = 0
    gift_dict = dict()
    gift_score = dict()
    answer_score = dict()
    
    for friend in friends:
        gift_dict[friend] = dict()
        for other_friend in friends:
            gift_dict[friend][other_friend] = 0
        gift_score[friend] = 0
        answer_score[friend] = 0
    
    for gift in gifts:
        giver, receiver = gift.split()
        gift_score[giver] += 1
        gift_score[receiver] -= 1
        gift_dict[giver][receiver] += 1
        
    for friend_me in friends:
        for friend_other in friends:
            if friend_me == friend_other:
                continue
            my_count = gift_dict[friend_me][friend_other]
            your_count = gift_dict[friend_other][friend_me]
            if my_count == your_count:
                if gift_score[friend_me] > gift_score[friend_other]:
                    answer_score[friend_me] += 1
            elif my_count > your_count:
                answer_score[friend_me] += 1

    return max(answer_score.values())
