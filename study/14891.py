import sys


def spin(direction, array):
    if direction == -1:
        left = array.pop(0)
        array.append(left)
    else:
        right = array.pop()
        array.insert(0, right)
    return array


def rotate(k, wheels, orders):
    for order in orders:
        # neighbors = []
        start_wheel = order[0] - 1  # 1 2 3 4 -> 0 1 2 3
        direction = order[1]
        # for j in range(4):
        #     if j % 2 == 0:
        #         neighbors.append(wheels[j][2])
        #     else:
        #         neighbors.append(wheels[j][6])
        for k in range(4):
            if start_wheel == 0



def score():
    points = 0

    return points


if __name__ == "__main__":
    read = sys.stdin.readline
    wheels = [list(map(int, read().rstrip())) for _ in range(4)]    # 0 1 2 3
    K = int(read())     # 회전수
    orders = [list(map(int, read().split()))]   # 번호, 방향(1:시계방향, -1:반시계방향)

