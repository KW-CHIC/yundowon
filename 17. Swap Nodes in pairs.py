# 페어의 노드 스왑

# 입력
# 1->2->3->4
# 출력
# 2->1->4->3

# 처음 풀이
from multiprocessing.connection import answer_challenge
import sys

num_list = list(sys.stdin.readline().split("->"))

answer = []

for i in range(0,len(num_list),2):
    answer.append(num_list[i + 1])
    answer.append(num_list[i])

print("->".join(answer))
