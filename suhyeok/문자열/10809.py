import sys

input = sys.stdin.readline

N = int(input())

paper = []
for i in range(N):
    paper.append(list(map(int, input().split())))

print(paper)
