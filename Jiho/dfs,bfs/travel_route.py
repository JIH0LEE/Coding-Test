from collections import deque

def recursion(route,routes,notVisited,answers,n):
    if len(route)==n:
        answers.append(list(route))

    else:
        src=route[-1]

        if src in routes:
            for next in routes[src]:
                if notVisited[(src,next)]:
                    route.append(next)
                    notVisited[(src,next)]-=1
                    recursion(route,routes,notVisited,answers,n)
                    route.pop()
                    notVisited[(src,next)]+=1
                

def solution(tickets):
    routes=dict()
    notVisited=dict()
    for elem in tickets:
        src,dst=elem
        if (src,dst) in notVisited:
            
            notVisited[(src,dst)]+=1
        else:
            notVisited[(src,dst)]=1
        if src in routes:
            routes[src].append(dst)
        else:
            routes[src]=[dst]
    answers=[]
    n=len(tickets)+1
    recursion(["ICN"],routes,notVisited,answers,n)
        

    answers.sort()
    answer=answers[0]
    return answer


solution([["ICN", "SFO"], ["SFO", "ICN"], ["ICN", "SFO"], ["SFO", "QRE"]])