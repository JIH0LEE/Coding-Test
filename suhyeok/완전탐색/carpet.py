def solution(brown, yellow):
    sum = brown + yellow
    answer = []
    for width in range(3, brown):
        if sum % width == 0:
            height = sum // width
            if (width - 2)*(height-2) == yellow:
                answer = [width, height]

    answer.sort(reverse=True)
    return answer
