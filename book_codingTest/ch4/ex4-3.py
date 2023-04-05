import sys


def solution(current):
    cnt = 0
    steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    x = int(ord(current[0])) - int(ord('a')) + 1
    y = int(current[1])
    for step in steps:
        nx = x + step[0]
        ny = y + step[1]
        if nx < 1 or ny < 1 or nx > 8 or ny > 8:
            continue
        else:
            cnt += 1
    return cnt


if __name__ == '__main__':
    read = sys.stdin.readline
    current = read()
    ans = solution(current)
    print(ans)
    