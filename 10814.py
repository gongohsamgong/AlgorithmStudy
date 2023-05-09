import sys


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    members = [list(read().split()) for _ in range(N)]
    members.sort(key=lambda x: int(x[0]))
    for member in members:
        print(member[0], member[1])
