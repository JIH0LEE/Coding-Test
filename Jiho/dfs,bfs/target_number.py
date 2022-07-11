#프로그래머스
#bfs,dfs
#타켓 넘버
def solution(numbers, target):
    n=len(numbers)
    stack=[(0,0)]
    answer = 0
    while stack:
        step,value=stack.pop()
        if step==n:
            if value==target:
                answer+=1
            continue
        stack.append((step+1,value+numbers[step]))
        stack.append((step+1,value-numbers[step]))
    return answer