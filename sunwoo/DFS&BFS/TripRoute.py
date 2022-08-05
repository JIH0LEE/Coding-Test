from collections import defaultdict
#스택
# 알파벳은 pop 뒤에서 빠짐 -> sort 사용

def solution(tickets):
    answer = []
    routes = defaultdict(list)
    
    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])
        
    for key in routes.keys():
        routes[key].sort(reverse=True)
        
    stack = ['ICN']
    while stack:
        tmp = stack[-1]
        
        if not routes[tmp]:
            answer.append(stack.pop())
        else:
            stack.append(routes[tmp].pop())
    answer.reverse()
    
    return answer
