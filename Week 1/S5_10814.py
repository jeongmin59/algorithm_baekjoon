# 10814번 나이순 정렬
# 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬

# 첫째 줄에는 회원의 수 N
# 둘째 줄부터는 회원의 나이와 이름이 공백으로 구분되어 주어짐
# 1 <= 나이 <= 200, 이름은 알파벳 대소문자로 이루어짐
# 입력은 가입한 순서로 주어짐

import sys
input = sys.stdin.readline

N = int(input().rstrip())

member = []

for i in range(N):
    age, name = map(str, input().rsplit())
    member.append([int(age), name])

member.sort(key=lambda x: x[0])

for j in member:
    print(j[0],j[1])