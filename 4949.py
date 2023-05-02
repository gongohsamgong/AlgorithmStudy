import sys


def solution(sentence):
    stack = []
    for i in range(len(sentence)):
        # print(stack)
        if sentence[i] == '(':
            stack.append('(')
        elif sentence[i] == '[':
            stack.append('[')
        elif sentence[i] == ')' and len(stack) != 0:
            if stack[-1] == '(':
                stack.pop()
            else:
                return 'no'
        elif sentence[i] == ']' and len(stack) != 0:
            if stack[-1] == '[':
                stack.pop()
            else:
                return 'no'
        else:
            continue
    if len(stack) == 0:
        return 'yes'
    else:
        return 'no'


if __name__ == "__main__":
    read = sys.stdin.readline
    ans = []
    while True:
        sentence = read()
        # print(sentence)
        if sentence == '.':
            break
        print(solution(sentence))
        ans.append(solution(sentence))
    print(*ans)
