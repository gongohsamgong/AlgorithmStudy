def add_date(term_date, today, months):  # 약관날짜, 오늘날짜, 계약기간
    t_y = int(today.split('.')[0])  # today's year
    t_m = int(today.split('.')[1])
    t_d = int(today.split('.')[2])
    p_y = int(term_date.split('.')[0])
    p_m = int(term_date.split('.')[1])
    p_d = int(term_date.split('.')[2])
    res_d = t_d
    if t_m + int(months) > 12:
        res_m = t_m + int(months) - 12
        res_y = t_y + 1
    else:
        res_m = t_m + int(months)
        res_y = t_y

    if res_y < t_y:
        return 'expire'
    elif res_y > t_y:
        return 'keep'
    else:  # res_y == t_y
        if res_m < t_m:
            return 'expire'
        elif res_m > t_m:
            return 'keep'
        else:  # res_m == t_m
            if res_d <= t_d:
                return 'expire'
            else:
                return 'keep'


def solution(today, terms, privacies):
    answer = []
    for i in range(len(privacies)):
        privacy_date = privacies[i].split(' ')[0]
        privacy_term = privacies[i].split(' ')[1]
        for j in range(len(terms)):
            term = terms[j].split(' ')
            if privacy_term == term[0]:
                result = add_date(privacy_date, today, term[1])
                if result == 'expire':
                    answer.append(i + 1)
                else:
                    continue

    return answer
