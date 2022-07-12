def solution(triangle):
    answer = 0
    # 0번째 줄 1
    # 1번째 줄 2
    # 2번째 줄 3
    n = len(triangle)
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]

            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]

            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    answer = max(triangle[-1])
    return answer
