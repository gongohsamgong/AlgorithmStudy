from collections import deque


def solution(maps):
    answer = []
    queue = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    temp = 0
    height = len(maps)
    width = len(maps[0])
    for i in range(height):
        for j in range(width):
            if maps[i][j] != 'X':
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        temp += maps[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < height and 0 <= ny < width and maps[nx][ny] != 'X':
                queue.append((nx, ny))
    if answer == 0:
    
    return answer
