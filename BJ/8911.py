from collections import deque
import sys

def solution(order):
    direc = 0 # 북0, 서1, 남2, 동3
    x, y = 0, 0
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    min_x, min_y, max_x, max_y = 0, 0, 0, 0
    
    for i in order:
        if i == 'F':
            x += dx[direc]
            y += dy[direc]
        elif i == 'B':
            x -= dx[direc]
            y -= dy[direc]
        elif i == 'L':
            if direc == 3:
                direc = 0
            else:
                direc += 1
        elif i == 'R':
            if direc == 0:
                direc = 3
            else:
                direc -= 1
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    
    return (abs(max_x - min_x) * abs(max_y - min_y))

if __name__ == '__main__':
    read = sys.stdin.readline
    t = int(read())
    graph = []
    ans = []
    for i in range(t):
        graph.append(list(map(str, read().rstrip())))
    for i in range(t):
        ans.append(solution(graph[i]))
        print(ans[i])
        
