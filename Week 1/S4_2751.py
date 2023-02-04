# 2751번 수 정렬하기 2
# N개의 수가 주어졌을 때, 오름차순으로 정렬하는 프로그램 작성

import sys
input = sys.stdin.readline

N = int(input().rstrip())

num = []

for _ in range(N):
    n = int(input().rstrip())
    num.append(n)

num.sort()

for i in num:
    print(i)
