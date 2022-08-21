# 두 정렬 리스트의 병합

# 입력
# 1->2->4
# 1->3->4
# 출력
# 1->1->2->3->4->4

# 처음 풀이
import sys

num_list1 = list(sys.stdin.readline().split("->"))
num_list2 = list(sys.stdin.readline().split("->"))

num_list1 += num_list2

num_list1.sort()

print(num_list1)

print("->".join(num_list1))
