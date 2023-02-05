# 1181번 단어 정렬

# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램 작성
# 1. 길이가 짧은 것부터 2. 길이가 같으면 사전 순으로

# 첫째 줄에 단어의 개수 N이 주어짐
# 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어짐

import sys
input = sys.stdin.readline

N = int(input().rstrip())

alphabet = []
for _ in range(N):
    a = input().rstrip().split()
    alphabet.append(a)

alphabet = sum(alphabet, [])
alpha = list(set(alphabet))
alpha.sort()
alpha.sort(key = len)

for i in alpha:
    print(i)
