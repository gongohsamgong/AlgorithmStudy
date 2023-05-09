from collections import deque


def bfs(place):
    locations = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                locations.append([i, j])  # [0,0],[0,4] ···

    for location in locations:
        queue = deque([location])
        visited = [[0] * 5 for _ in range(5)]
        distance = [[0] * 5 for _ in range(5)]
        visited[location[0]][location[1]] = 1

        while queue:
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            y, x = queue.popleft()

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= nx < 5 and 0 <= ny < 5 and visited[ny][nx] == 0:
                    distance[ny][nx] = distance[y][x] + 1
                    if place[ny][nx] == 'O':
                        queue.append([ny, nx])
                        visited[ny][nx] = 1
                    if place[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(bfs(place))

    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
ans = solution(places)
print(ans)
