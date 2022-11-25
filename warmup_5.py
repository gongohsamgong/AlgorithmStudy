def solution(bar):
    stack = []
    answer = 0
    for i in range(len(bar)):
        if bar[i] == '(':
            stack.append('(')
        else:
            stack.pop()
            if bar[i - 1] == '(':
                answer += len(stack)
            else:
                answer += 1

    return answer
