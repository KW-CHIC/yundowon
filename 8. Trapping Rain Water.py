# 빗물 트래핑

# 입력
# 0 1 0 2 1 0 1 3 2 1 2 1
# 출력
# 6

# 처음 풀이

import sys

num_list = list(map(int,sys.stdin.readline().split()))

answer = 0

volume = 0
left, right = 0, len(num_list) - 1

left_max, right_max = num_list[left], num_list[right]

while left < right:
    left_max, right_max = max(num_list[left], left_max), max(num_list[right], right_max)

    if left_max <= right_max:
        volume += left_max - num_list[left]
        left += 1
    else:
        volume += right_max - num_list[right]
        right -= 1

print(volume)
