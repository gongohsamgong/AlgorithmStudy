import sys


if __name__ == '__main__':
    read = sys.stdin.readline
    word = read().rstrip()
    croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    for alphabet in croatia:
        word = word.replace(alphabet, '_')
    print(len(word))
