# 2839번 설탕 배달
# 상근이는 설탕을 정확하게 N개 배달해야 함. 봉지는 3kg, 5kg이 있음
# 최대한 적은 봉지를 들고 가려고 함. 몇 개를 들고 가면 되는지 작성
# 정확하게 Nkg을 만들 수 없다면 -1 출력

import sys
input = sys.stdin.readline

N = int(input().rstrip())

if N % 5 == 0:      # 5로 나누었을 때
    print(N // 5)

elif N % 5 == 3:    # 5로 나누었을 때 3인 경우 예를 들어 8, 13 등...
    print(int(N // 5 + 1))  # 몫에 + 1 하면 3kg도 되니까... 예시 8 -> 2개

elif N % 5 <= 4 and N % 3 == 0: # 5로도 나누어지고 3으로 나누었을 때
    print(N // 3)

elif N % 5 <= 3 and N % 3 == 2: # 5로 나누어지는 것과 3으로 나눠지는 것
    print(int(N % 5 + N % 3))

else:
    print(-1)

# 입력 예시를 넣으면 맞는데 제출하면 왜 틀렸을까