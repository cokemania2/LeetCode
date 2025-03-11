# 유효기간

from datetime import datetime
from dateutil.relativedelta import relativedelta

def get_end_date(d, term, terms_month):
    valid_month = terms_month[term]
    
    start_date = datetime.strptime(d, "%Y.%m.%d")
    end_date = start_date + relativedelta(months=valid_month)
    
    return end_date.strftime("%Y.%m.%d")


def solution(today, terms, privacies):
    answer = []

    terms_month = dict()
    for term in terms:
        term, month = term.split()
        terms_month[term] = int(month)
    
    for i, privacie in enumerate(privacies):
        _date, term = privacie.split()
        end_date = get_end_date(_date, term, terms_month)
        
        if end_date <= today:
            answer.append(i + 1)
    
    return answer