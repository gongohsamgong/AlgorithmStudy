from collections import deque
import sys

def solution(q, visited, s):
    while q:
        now, clip = q.popleft()
        if now == s:
            return visited[(now, clip)]
        if (now, now) not in visited.keys():
            visited[(now, now)] = visited[(now, clip)] + 1
            q.append((now, now))
        if (now + clip, clip) not in visited.keys():
            visited[(now + clip, clip)] = visited[(now, clip)] + 1
            q.append((now + clip, clip))
        if (now - 1, clip) not in visited.keys():
            visited[(now - 1, clip)] = visited[(now, clip)] + 1
            q.append((now - 1, clip))
    

if __name__ == '__main__':
    read = sys.stdin.readline
    s = int(read())
    q = deque()
    q.append((1, 0))
    visited = dict()
    visited[(1, 0)] = 0
    ans = solution(q, visited, s)
    print(ans)
