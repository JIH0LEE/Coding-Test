import sys
from collections import Counter

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()
c_c = Counter(arr).most_common()
print(round(sum(arr) / n))
print(arr[n // 2])

if len(c_c) > 1:
    if c_c[0][1] == c_c[1][1]:
        print(c_c[1][0])
    else:
        print(c_c[0][0])
else:
    print(c_c[0][0])

print(max(arr) - min(arr))
