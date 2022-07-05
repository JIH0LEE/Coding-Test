
# %%
def fib(n):
    count = 0
    if n == 1 or n == 2:
        count += 1
        return count
    else:
        return fib(n-1)+fib(n-2)

# %%


def fibonacci(n):
    fb = [0 for i in range(n+1)]
    fb[1] = fb[2] = 1
    cnt = 0

    for i in range(3, n+1):
        fb[i] = fb[i-1]+fb[i-2]
        cnt += 1
    return cnt


# %%
n = int(input())
print(fib(n), fibonacci(n))

# %%
