def solution(s):
    answer = True
    stack = []
    if s[0] == ')':
        return False
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            if len(stack) == 0:
                return False
            else:
                if stack.pop() != '(':
                    return False
        if i == len(s) - 1:
            if len(stack) != 0:
                answer = False
    return answer
