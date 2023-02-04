# 1978번 소수 찾기
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력

# N <= 100 , N개의 수 <= 1000

# 주어진 수들 중 소수의 개수 출력


import sys
input = sys.stdin.readline

N = input().rstrip()
num = list(map(int, input().rstrip().split()))

sosu = []

for n in num:
    for i in range(2, n + 1):   # 2이상부터 n까지
        if n % i == 0:          # n을 3~n까지 나눴을 때 나머지가 0이면 소수라고 생각했음
            sosu.append(n)

print(len(sosu))

# 예시 케이스는 맞는데, 제출했을 때 틀렸다고 함

# 1과 자기자신으로 나누어짐. 다른 수로 나누어지면 소수 아님
# 2부터 1을 뺀 숫자까지 나눴을 때 나머지가 0이 안 된다면 소수가 아님