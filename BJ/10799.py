import sys


def solution(lst):
    ans = 0
    stack = []

    for i in range(len(lst)):
        if lst[i] == '(':
            stack.append(lst[i])
        else:
            stack.pop()
            if lst[i - 1] == '(':
                ans += len(stack)
            else:
                ans += 1
    return ans


if __name__ == '__main__':
    lst = sys.stdin.readline().strip()
    answer = solution(lst)
    print(answer)
