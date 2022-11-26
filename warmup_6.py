def solution(log):
    answer = []
    for i in range(len(log)):
        if log[i] == '<':
            if i == 0 or i == len(log) - 1:
                continue
            else:
                answer.insert(len(answer) - 1, log[i])
        elif log[i] == '>':
            if i == 0 or i == len(log) - 1:
                continue
            else:
                answer.insert(0, log[i])
        elif log[i] == '-':
            answer.pop()

        answer.append(log[i])

    res = ''
    for j in range(len(answer)):
        res += str(answer[i])
    return res
