# 브루트 포스로 계산
# * 입력 
# 2 7 11 15
# 9
# 출력
# [0,1]

'''
# 처음 풀이

import sys

num_list = list(map(int,sys.stdin.readline().split()))

num = int(sys.stdin.readline())

for i in range(len(num_list) - 1):
    if num_list[i] + num_list[i + 1] == num:
        print([i,i+1])
        break

'''

'''
# in을 이용한 탐색

import sys

num_list = list(map(int,sys.stdin.readline().split()))

num = int(sys.stdin.readline())

for i, n in enumerate(num_list):
    temp = num - n
    if temp in num_list[i + 1:]:
        print([i,i+1])
        break


'''


'''
# 첫번째 수를 뺀 결과 키 조회

import sys

num_list = list(map(int,sys.stdin.readline().split()))

num = int(sys.stdin.readline())

num_map = {}

for i, ele in enumerate(num_list):
    num_map[ele] = i

for i, ele in enumerate(num_list):
    if num - ele in num_map and i != num_map[num - ele]:
        print([i,num_map[num - ele]])
        break

'''

'''
#  위의 풀이 최적화

import sys

num_list = list(map(int,sys.stdin.readline().split()))

num = int(sys.stdin.readline())

num_map = {}

for i, ele in enumerate(num_list):
    if num - ele in num_map:
        print([i,num_map[num - ele]])
        break
    num_map[ele] = i

'''

# 투 포인터 이용
# 너무 비효율적

#방식은 왼쪽 포인터와 오른쪽 포인터의 합이 타켓보다 크다면 오른쪽 포인터를 왼쪽으로 왼쪽은 오른쪽으로 이동


