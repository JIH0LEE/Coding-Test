
# %%
n = int(input())

# %%
for j in range(n):
    k = int(input())
    pv = [0 for i in range(101)]
    pv[0] = pv[1] = pv[2] = 1
    pv[3] = pv[4] = 2

    for i in range(5, 101):
        pv[i] = pv[i-1]+pv[i-5]

    print(pv[k-1])

# %%
