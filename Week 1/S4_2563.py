# 2563번 색종이
# 가로, 세로 크기가 100인 정사각형 도화지 위에 가로, 세로 크기가 각각 10인 정사각형을 평행하도록 붙임
# 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램 작성

import sys
input = sys.stdin.readline

N = int(input().rstrip())

for _ in range(N):
    x, y = map(int, input().rstrip().split())

# 색종이 넓이 (x+10)-x * (y+10)- y
# 겹치는 영역을 구하려면... 원래 흰 도화지 사각형 - 안 겹치는 사각형