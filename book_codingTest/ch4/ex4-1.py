import sys


def solution(n, array):
    x, y = 1, 1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']
    for direction in array:
        for i in range(4):
            if direction == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny
    return x, y


if __name__ == '__main__':
    read = sys.stdin.readline
    N = int(read())
    directions = list(read().split())
    ans = solution(N, directions)
    print(ans)
