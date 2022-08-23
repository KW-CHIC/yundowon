# 홀짝 연결 리스트

# 입력
# 1->2->3->4->5->NULL
# 출력
# 1->3->5->2->4->NULL

# 처음 풀이
from multiprocessing.connection import answer_challenge
import sys

num_list = list(sys.stdin.readline().split("->"))

answer = []

for i in range(0,len(num_list),2):
    answer.append(num_list[i])
for i in range(1,len(num_list),2):
    answer.append(num_list[i])

print("->".join(answer))
