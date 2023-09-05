import sys


def solution(n, array):
    stack, ans = [], []
    current = 1
    for i in range(n):
        while current <= array[i]:
            stack.append(current)
            ans.append('+')
            current += 1

        if stack[-1] == array[i]:
            stack.pop()
            ans.append('-')
        else:
            ans = ['NO']
            return ans
    return ans


if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    numbers = [int(read()) for _ in range(n)]
    answer_list = solution(n, numbers)
    for answer in answer_list:
        print(answer)
