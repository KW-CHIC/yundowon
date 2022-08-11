# 세 수의 합

# 입력
# -1 0 1 2 -1 -4
# 출력
# 6

# 처음 풀이

import sys

num_list = list(map(int,sys.stdin.readline().split()))

num_list.sort()

for i in range(len(num_list) - 2):

    if i>0 and num_list[i] == num_list[i-1]:
        continue
    
    left, right = i + 1, len(num_list) - 1

    while right > left:
        sum = num_list[i] + num_list[right] + num_list[left]
        if sum < 0:
            left += 1
        elif sum > 0:
            right -= 1
        else:
            print([num_list[i], num_list[right], num_list[left]])
            left += 1
            right -= 1
            
