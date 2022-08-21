# 두수의 덧셈

# 입력
# (2->4->3)+(5->6->4)
# 출력
# 7->0->8

# 처음 풀이
from multiprocessing.connection import answer_challenge
import sys

num_list = sys.stdin.readline()

num_list = num_list.replace("+","->")

num_list = list(num_list.split("->"))

print(num_list)
temp = []
answer = 0

for i in num_list:

    if "(" in i:
        temp.append(i[1])
    elif ")" in i:
        temp.append(i[0])
        temp.reverse()
        answer += int("".join(temp))
        temp = []
    else:
        temp.append(i)

answer = list(str(answer))

answer.reverse()

print("->".join(answer))
