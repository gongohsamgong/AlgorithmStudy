import sys
from collections import deque


if __name__ == "__main__":
    read = sys.stdin.readline
    queue = deque()
    N = int(read())
    commands = [list(read().split()) for _ in range(N)]
    for command in commands:
        if command[0] == 'push':
            queue.append(int(command[1]))
        elif command[0] == 'pop':
            if len(queue) == 0:
                print(-1)
            else:
                out = queue.popleft()
                print(out)
        elif command[0] == 'size':
            print(len(queue))
        elif command[0] == 'empty':
            if len(queue) == 0:
                print(1)
            else:
                print(0)
        elif command[0] == 'front':
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[0])
        else:
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[-1])
