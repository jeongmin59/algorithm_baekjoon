# 5635번 생일

# 가장 나이가 적은 사람과 가장 많은 사람을 구하는 프로그램 작성

# 첫째 줄에 반에 있는 학생의 수 n
# 다음 n개 줄에는 각 학생의 이름과 생일이 "이름 dd mm yyyy" 형식으로 주어짐
# 이름은 최대 15글자, 생일은 일, 월, 연도
# 이름이 같거나, 생일이 같은 사람은 없음

# 첫째 줄에 가장 나이가 적은 사람의 이름, 둘째 줄에 가장 나이가 많은 사람 이름 출력

import sys
input = sys.stdin.readline

N = int(input().rstrip())

student = []

for _ in range(N):
    name, d, m, y = map(str, input().rstrip().split())
    d, m, y = map(int, (d, m, y))
    student.append([y, m, d, name])

student.sort()

print(student[-1][-1])
print(student[0][-1])

