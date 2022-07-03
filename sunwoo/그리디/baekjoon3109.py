# 빵집
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(input().strip()))

dx = [-1, 0, 1]
dy = [1, 1, 1]


def pipe(x, y):
    global result
    arr[x][y] = 'o'
    if y == M-1:
        result += 1
        return True
    for k in range(3):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] != 'x' and arr[nx][ny] != 'o':
                if pipe(nx, ny):
                    return True


result = 0
for i in range(N):
    pipe(i, 0)
print(result)
