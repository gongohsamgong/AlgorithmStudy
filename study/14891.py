import sys
import math


def spin(direction, array):
    if direction == -1:
        left = array.pop(0)
        array.append(left)
    else:
        right = array.pop()
        array.insert(0, right)
    return array


def score(wheels):
    point = 0
    for i in range(4):
        if wheels[i][0] == 1:
            # print(math.pow(2, i))
            point += int(math.pow(2, i))
            # print(point)
    return point


def rotate(k, wheels, orders):
    for order in orders:
        neighbors = []
        start_wheel = order[0] - 1  # 1 2 3 4 -> 0 1 2 3
        direction = order[1]
        direct = order[1]
        for i in range(4):
            neighbors.append([wheels[i][6], wheels[i][2]])

        # left
        for i in range(start_wheel-1, -1, -1): # 0, 1, .. startwheel-1 까지
            # print('left :', i+1)
            if neighbors[i][1] != neighbors[i+1][0]:
                wheels[i] = spin(-direction, wheels[i])
                direction *= (-1)
            else:
                break
        # right
        for i in range(start_wheel+1, 4):
            # print('right :', i+1)
            if neighbors[i-1][1] != neighbors[i][0]:
                wheels[i] = spin(-direction, wheels[i])
                direction *= (-1)
            else:
                break
        wheels[start_wheel] = spin(direct, wheels[start_wheel])
        # print(wheels)
    return score(wheels)


if __name__ == "__main__":
    read = sys.stdin.readline
    wheels = [list(map(int, read().rstrip())) for _ in range(4)]    # 0 1 2 3
    K = int(read())     # 회전수
    orders = [list(map(int, read().split())) for _ in range(K)]   # 번호, 방향(1:시계방향, -1:반시계방향)
    ans = rotate(K, wheels, orders)
    print(ans)
