'''
반복문의 중쳡을 피하기 위해 함수화하여 쪼개는 것을 지향해야하지만,,, 아직 미숙해서 오류가 나더라구요ㅠㅠ
다음주부터는 체계적으로 짤 수 있도록 조금 더 노력하겠습니다!
'''
def solution(grid):
    answer = []
    dy = [1, 0, -1, 0]
    dx = [0, -1, 0, 1]

    ly, lx = len(grid), len(grid[0])

    visited = [[[False] * 4 for _ in range(lx)] for _ in range(ly)]

    for y in range(ly):
        for x in range(lx):
            # d = [0, 1, 2, 3] == [위, 오른, 아래, 왼]
            for direction in range(4):
                if visited[y][x][direction]:
                    continue
                count = 0
                ny, nx = y, x
                while not visited[ny][nx][direction]:
                    visited[ny][nx][direction] = True
                    count += 1
                    if grid[ny][nx] == 'S':
                        pass
                    elif grid[ny][nx] == 'L':
                        direction = (direction - 1) % 4
                    elif grid[ny][nx] == 'R':
                        direction = (direction + 1) % 4
                    ny = (ny + dy[direction]) % ly
                    nx = (nx + dx[direction]) % lx
                answer.append(count)
    answer = sorted(answer)
    return answer
