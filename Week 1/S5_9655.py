# 9655번 돌 게임

# 돌 N개 있음. 상근이와 창영이는 턴을 번갈아가면서 돌을 가져가며,
# 돌은 1개 or 3개 가져갈 수 있음. 마지막 돌을 가져가는 사람이 이긴다.
# 이기는 사람 프로그램을 작성. 게임은 상근이가 먼저 시작

# 상근이가 이기면 SK를, 창영이가 이기면 CY를 출력

import sys
input = sys.stdin.readline

N = int(input().rstrip())

if N % 2 == 0:
    print("CY")
else:
    print("SK")
