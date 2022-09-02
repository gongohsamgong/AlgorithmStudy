def location(x_, y_, n_):
    if (0 < x_ < n_ + 1) and (0 < y_ < n_ + 1):
        return True
    else:
        return False


def move(x_, y_, n_, way):
    if way == 'L' and location(x_, y_-1, n_):
        y_ -= 1
    elif way == 'R' and location(x_, y_+1, n_):
        y_ += 1
    elif way == 'U' and location(x_-1, y_, n_):
        x_ -= 1
    elif way == 'D' and location(x_+1, y_, n_):
        x_ += 1
    return x_, y_


if __name__ == '__main__':
    n = int(input())
    direction = input().split()
    x = y = 1
    for i in range(len(direction)):
        x, y = move(x, y, n, direction[i])
    print(x, y)