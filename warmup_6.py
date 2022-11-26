def solution(log):
    answer = ''
    front = list()
    back = list()

    for c in log:
        if c == '-':
            if front:
                front.pop()
        elif c == '<':
            if front:
                back.append(front.pop())
        elif c == '>':
            if back:
                front.append(back.pop())
        else:
            front.append(c)

    answer = ''.join(front) + ''.join(back[::-1])
    return answer
