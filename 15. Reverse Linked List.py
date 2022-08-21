# 역순 연결 리스트

# 입력
# 1->2-3->4->5->NULL
# 출력
# 5->4->3->2->1->NULL

# 처음 풀이
import sys

num_list = list(sys.stdin.readline().split("->"))

temp = num_list.pop()

num_list.reverse()

num_list.append(temp)

print("->".join(num_list))
