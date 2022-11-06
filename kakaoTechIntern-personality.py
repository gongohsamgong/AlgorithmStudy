def choice_score(n):
    a = 0
    b = 0
    if n == 1:
        a += 3
    elif n == 2:
        a += 2
    elif n == 3:
        a += 1
    elif n == 5:
        b += 1
    elif n == 6:
        b += 2
    elif n == 7:
        b += 3
    return a, b


def solution(survey, choices):
    answer = ''
    res = [0] * 8
    for i in range(len(survey)):
        if survey[i][0] == 'R':
            a, b = choice_score(choices[i])
            res[0] += a
            res[1] += b
        elif survey[i][0] == 'T':
            a, b = choice_score(choices[i])
            res[0] += b
            res[1] += a
        elif survey[i][0] == 'C':
            a, b = choice_score(choices[i])
            res[2] += a
            res[3] += b
        elif survey[i][0] == 'F':
            a, b = choice_score(choices[i])
            res[2] += b
            res[3] += a
        elif survey[i][0] == 'J':
            a, b = choice_score(choices[i])
            res[4] += a
            res[5] += b
        elif survey[i][0] == 'M':
            a, b = choice_score(choices[i])
            res[4] += b
            res[5] += a
        elif survey[i][0] == 'A':
            a, b = choice_score(choices[i])
            res[6] += a
            res[7] += b
        elif survey[i][0] == 'N':
            a, b = choice_score(choices[i])
            res[6] += b
            res[7] += a

    if res[0] < res[1]:
        answer += 'T'
    else:
        answer += 'R'
    if res[2] < res[3]:
        answer += 'F'
    else:
        answer += 'C'
    if res[4] < res[5]:
        answer += 'M'
    else:
        answer += 'J'
    if res[6] < res[7]:
        answer += 'N'
    else:
        answer += 'A'

    return answer
