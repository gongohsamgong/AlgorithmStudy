import sys


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    commands = [list(read().split()) for _ in range(N)]
    stack = []
    for command in commands:
        if command[0] == 'push':
            stack.append(int(command[1]))
        elif command[0] == 'pop':
            if len(stack) == 0:
                print(-1)
            else:
                out = stack.pop()
                print(out)
        elif command[0] == 'size':
            print(len(stack))
        elif command[0] == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif command[0] == 'top':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
