import sys

if __name__ == "__main__":
    read = sys.stdin.readline
    i = 1

    while True:
        L, P, V = map(int, read().split())

        if L + P + V == 0:
            break

        result = (V // P) * L
        result += min(V % P, L)
        print('Case %d: %d' % (i, result))
        i += 1
