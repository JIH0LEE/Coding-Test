def solution(number, k):
    answer = ''
    stack = []

    for num in number:
        while stack and k > 0 and stack[-1] < num:
            stack.pop(-1)
            k -= 1
        stack.append(num)
    stack = stack[:len(stack)-k]
    answer = ''.join(stack)

    return answer
