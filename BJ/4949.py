import sys


def solution(sentence):
    stack = []
    for letter in sentence:
        if letter == '(' or letter == '[':
            stack.append(letter)
        elif letter == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
        elif letter == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
    if len(stack) == 0:
        print('yes')
    else:
        print('no')


if __name__ == "__main__":
    read = sys.stdin.readline
    ans = []
    while True:
        sentence = read().rstrip()
        if sentence == '.':
            break
        else:
            solution(sentence)
