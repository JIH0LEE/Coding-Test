def solution(number, k):
    lst = []
    
    for i, v in enumerate(number):
        while lst and lst[-1] < v and k > 0:
            lst.pop()
            k -= 1
        
        if k == 0:
            lst.extend([x for x in number[i:]])
            break
        lst.append(v)
        
    lst = (lst[:-k] if k > 0 else lst)
        
    return ''.join(lst)