# 15904번 UCPC는 무엇의 약자일까?
# UCPC는 전국 대학생 프로그래밍 대회 동아리 연합 여름 대회의 줄임말
# 문자열을 적절히 축약해서 UCPC로 만들 수 있는지 확인하는 프로그램 만들기
# 문자열을 비교할 때 대소문자를 구분해 정확히 비교함

# UCPC로 만들 수 있으면 "I love UCPC", 만들 수 없으면 "I hate UCPC"

import sys
input = sys.stdin.readline

sentence = input().rstrip().split()

ucpc = ['U','C','P', 'C']
cnt = 0

for w in sentence:
    if w[0] == ucpc[0]:
        cnt += 1 
    if w[0] == ucpc[1] or w[0] == ucpc[3]:
        cnt += 1 
    if w[0] == ucpc[2]:
        cnt += 1 
if cnt == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")

# 예시 넣을 땐 맞는데, 어느 부분에서 틀렸다고 뜨는거임?