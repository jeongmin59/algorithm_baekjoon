# 1065번 한수
# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면 한수라고 함
# 등차수열 = 연속된 2개의 수의 차이가 일정한 수열을 말함
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력

# 123 -> 1,2,3 => 한수임 123 -> 1~9까지도 다 한수

import sys
input = sys.stdin.readline

N = int(input().rstrip())

hansu = 0

for n in range(1, N + 1):
    if n <= 99:     # 1부터 99까지는 모두 한수
        hansu += 1
    else:
        N = list(map(int, str(n)))  # 자릿수대로 분리
        if N[0] - N[1] == N[1] - N[2] : # 등차수열 확인
            hansu += 1

# 문제 이해하는게 힘들었습니다...